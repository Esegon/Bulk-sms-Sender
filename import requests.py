import requests
import json

api_key = "7c31578aaede4ef0aa78e803756293e77e5bb81d56ffe02bb52df68d72e963fc"
sender_id = "23107"
recipient_numbers = ["+254754373914"]
message = "Reach us on whatsapp using the link below https://wa.me/+254706370318.\n\nRegards,\nEsegon"

url = "https://api.mobitechtechnologies.com/sms/sendsms"

headers = {
    "h_api_key": api_key,
    "Content-Type": "application/json"
}

for number in recipient_numbers:
    payload = {
        "mobile": number,   
        "response_type": "json",
        "sender_name": sender_id,
        "service_id": 0,
        "message": message
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print(f"SMS sent successfully to {number}.")
        print("Response:", response.text)
    else:
        print(f"Failed to send SMS to {number}. Error:", response.text)
