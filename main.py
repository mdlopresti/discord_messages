import os
import requests

def main():
    if 'WEBHOOK' in os.environ:
        if 'MESSAGE' in os.environ:
            webhook = os.environ['WEBHOOK']
            message = os.environ['MESSAGE']
            username = os.environ.get('USERNAME', 'Notification')

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
        else:
            print('MESSAGE is a mandatory environment variable and is not set')
    else:
        print('WEBHOOK is a mandatory environment variable and is not set')
    
main()