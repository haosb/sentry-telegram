import os
import requests
from flask import Flask, request, abort

apiToken = os.getenv('TOKEN')
chatID = os.getenv('CHATID')
apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(f'Request json - {request.json}\n')
        message = request.json
        response = requests.post(apiURL, data={'chat_id': chatID, 'text': f"<b>Sentry Alert</b> 🔥\n\nProject - {message.get('project_name')}\nMessage - {message.get('message')}\nUrl - {message.get('url')}", 'parse_mode': 'html'})

        print(f'Telegram response - {response.text}')
        return 'Success', response.status_code
    else:
        abort(400)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
