import boto3
from botocore.exceptions import ClientError

# https://docs.aws.amazon.com/en_pv/ses/latest/DeveloperGuide/send-using-sdk-python.html

SENDER = "Dustin Test <dustin-test@lilly.com>"
RECIPIENT = "djefford@lilly.com"

AWS_REGION = "us-east-1"

SUBJECT = "Amazon SES Test (SDK for Python)"
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )

# BODY_HTML = """<html>
# <head></head>
# <body>
#   <h1>Amazon SES Test (SDK for Python)</h1>
#   <p>This email was sent with
#     <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
#     <a href='https://aws.amazon.com/sdk-for-python/'>
#       AWS SDK for Python (Boto)</a>.</p>
# </body>
# </html>
#             """

BODY_HTML = """
<h1>Landing Zone Account Notification<br>
---------------------------------------------</h1>
<h3>Account: ######</h3>
<h3>Region: ######</h3>
<p>The following resources in the account are not tagged properly. Please log into the Landing Zone account and take corrective action on the resources listed below.<br>
For a complete list, you can find Compliance results in the AWS Config Console (please ensure you are logged into the account specified above).</p>
<p><a href='https://aws.amazon.com/ses/'>Amazon SES</a></p>

<h4>Resource List
<br>-----------------</h4>
<p>ResourceID: </p>
<p>ResourceID: </p>
<h4>-----------------</h4>
<p>For questions about this communication, please submit an email to the Landing Zone team:<br>
<a href="mailto:fakeList@fake.com">FakeList@fake.com</a></p>
"""

CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

try:
  response = client.send_email(
    Destination={
      'ToAddresses': [
        RECIPIENT,
      ],
    },
    Message={
      'Body': {
        'Html': {
          'Charset': CHARSET,
          'Data': BODY_HTML,
        },
        'Text': {
          'Charset': CHARSET,
          'Data': BODY_TEXT,
        },
      },
      'Subject': {
        'Charset': CHARSET,
        'Data': SUBJECT,
      },
    },
    Source=SENDER,
  )

except ClientError as e:
  print(e.response['Error']['Message'])
else:
  print("Email sent! Message ID:"),
  print(response['MessageId']) 

