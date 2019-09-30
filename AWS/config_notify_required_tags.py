import boto3 as b3
import json
from datetime import datetime
from botocore.exceptions import ClientError

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)

# Global variables
client = b3.client('config')
# sns_client = b3.client('sns', region_name='us-east-2')

def get_compliance(filters):
    results = []
    paginator = client.get_paginator('describe_aggregate_compliance_by_config_rules')
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
        paginator = client.get_paginator('get_aggregate_compliance_details_by_config_rule')
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

def format_email(rule_evaluation):
    account = rule_evaluation['AccountId']
    region = rule_evaluation['AwsRegion']
    # Add header
    email_body = """
<h1>Landing Zone Account Notification<br>
---------------------------------------------</h1>
<h3>Account: {}</h3>
<h3>Region: {}</h3>
<p>The following resources in the account are not tagged properly. Please log into the Landing Zone account and take corrective action on the resources listed below.<br>
For a complete list, you can find Compliance results in the AWS Config Console (please ensure you are logged into the account specified above).</p>
<p><a href='https://{}.console.aws.amazon.com/config/home?region={}#/rules/rule-details/{}'>Rule Details</a></p>
<h4>Resource List
<br>-----------------</h4>
    """.format(account, region, region, region, "OrgConfigRule-LILLY_REQUIRED_TAGS-hkvnvupr")

# STOPPED WORK HERE
    for i in rule_evaluation['Evaluation']:
        email_body += ""

    # list resources

    return email_body


# End function definitions

non_compliant_rules = get_compliance({
    'ConfigRuleName':'OrgConfigRule-LILLY_REQUIRED_TAGS-hkvnvupr',
    'ComplianceType': 'NON_COMPLIANT'
})
rule_evaluation = describe_non_compliant_rules(non_compliant_rules)

for result in rule_evaluation:
    message = format_email(result)
    print(message)
