import boto3 as b3
import json
import pprint as p
from datetime import datetime
from botocore.exceptions import ClientError

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)

# Global variables
config_client = b3.client('config', region_name='us-east-2')
ses_client = b3.client('ses', region_name='us-east-1')

def get_compliance(filters):
    results = []
    paginator = config_client.get_paginator('describe_aggregate_compliance_by_config_rules')
    pages = paginator.paginate(
        ConfigurationAggregatorName='Organization-Aggregator',
        Filters=filters
    )
    for page in pages:
        for result in page['AggregateComplianceByConfigRules']:
            results.append(result)
    return results


def describe_non_compliant_rules(non_compliant_rules):
    rule_details = []
    for rule in non_compliant_rules:
        results = []
        paginator = config_client.get_paginator('get_aggregate_compliance_details_by_config_rule')
        pages = paginator.paginate(
            ConfigurationAggregatorName='Organization-Aggregator',
            ConfigRuleName=rule['ConfigRuleName'],
            AccountId=rule['AccountId'],
            AwsRegion=rule['AwsRegion'],
            ComplianceType='NON_COMPLIANT'
        )
        for page in pages:
            for result in page['AggregateEvaluationResults']:
                results.append(result)
        rule['Evaluation'] = results
        rule_details.append(rule)
    return rule_details


def format_ses_template_data(missing_tags_evaluation):
    account = missing_tags_evaluation['AccountId']
    region = missing_tags_evaluation['AwsRegion']
    config_rule_name = missing_tags_evaluation['ConfigRuleName']


    # meta_data = '"meta":{{ "account": "{}", "region": "{}" }}'.format(account, region)
    meta_data = '"account": "{}", "region": "{}", "ConfigRuleName": "{}"'.format(account, region, config_rule_name)
    resource_data = '"resource": ['

    count = 0           # Count used for placing "," in the for loop
    for i in missing_tags_evaluation['Evaluation']:
        resource_id = i['EvaluationResultIdentifier']['EvaluationResultQualifier']['ResourceId']
        annotation = i['Annotation']

        resource_data += '{{ "resource_id": "{}", "annotation": "{}" }}'.format(resource_id, annotation)
        if count < len(missing_tags_evaluation['Evaluation'])-1:
            resource_data += ","
        count += 1
    
    resource_data += "]"
    template_data = "{" + meta_data + "," + resource_data + "}"
    return template_data


def email_eval_results(recipient, template_data):
    sender = "Dustin Test <dustin-test@lilly.com>"
    template = "ComplianceEmailTemplateTest"

    response = ses_client.send_templated_email(
        Source=sender,
        Destination={
            'ToAddresses': [ recipient ]
        },
        Template=template,
        TemplateData=template_data,
        ConfigurationSetName="ses-event-failure"
    )



    return response


# End function definitions

non_compliant_rules = get_compliance({
    'ConfigRuleName':'OrgConfigRule-LILLY_REQUIRED_TAGS-hkvnvupr',
    'ComplianceType': 'NON_COMPLIANT'
})
rule_evaluation_results = describe_non_compliant_rules(non_compliant_rules)

template_data = format_ses_template_data(rule_evaluation_results[0])

# print(template_data)

email_response = email_eval_results("djefford@lilly.com", template_data)
print(email_response)
