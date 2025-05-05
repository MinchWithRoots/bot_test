from flask import Flask, request

app = Flask(__name__)

CONFIRMATION_TOKEN = 'f52f1088'

@app.route('/callback/xE4sA', methods=['POST'])
def vk_callback():
    data = request.json
    if data.get('type') == 'confirmation':
        return CONFIRMATION_TOKEN  # Вернуть токен подтверждения
    return 'ok'

if __name__ == '__main__':
    app.run(port=80)

