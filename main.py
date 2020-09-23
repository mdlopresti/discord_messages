import os
import requests

def main():
    webhook = os.environ['WEBHOOK']
    message = os.environ['MESSAGE']
    username = os.environ['USERNAME']

    payload = {
        'content': message,
        'username': username
    }
    discord_request = requests.post(webhook, data = payload)

    if discord_request.status_code == 204:
        print('Successfully sent')
    else:
        print(discord_request.status_code)
        print(discord_request.text)

main()