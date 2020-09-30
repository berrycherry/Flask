import json
import os
import requests


def send_email(receiver_email, subject, text):
    sender_email = os.getenv("MY_SENDER_EMAIL")  # Your website's official email address
    api_key = os.getenv('SENDGRID_API_KEY')

    sender_email = "elvira.newzealand@gmail.com"
    api_key = "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"

    if not sender_email or not api_key:
        print("No env vars or no email address")
        return

    url = "https://api.sendgrid.com/v3/mail/send"

    data = {"personalizations": [{
                "to": [{"email": receiver_email}],
                "subject": subject
            }],

            "from": {"email": sender_email},

            "content": [{
                "type": "text/plain",
                "value": text
            }]
    }

    headers = {
        'authorization': "Bearer {0}".format(api_key),
        'content-type': "application/json"
    }

    response = requests.request("POST", url=url, data=json.dumps(data), headers=headers)

    print("Sent to SendGrid")
    print(response.text)
