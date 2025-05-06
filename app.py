from flask import Flask, request
import json
import random
import vk

app = Flask(__name__)

# Токены из настроек твоей группы
confirmation_token = 'f52f1088'  # Токен для подтверждения от VK
token = 'ВАШ_ТОКЕН_ГРУППЫ'       # Токен для отправки сообщений

@app.route('/callback', methods=['POST'])
def processing():
    data = json.loads(request.data)

    if 'type' not in data:
        return 'not vk'

    if data['type'] == 'confirmation':
        return confirmation_token

    elif data['type'] == 'message_new':
        user_id = data['object']['message']['from_id']

        session = vk.Session()
        api = vk.API(session, v='5.110')

        api.messages.send(
            access_token=token,
            user_id=str(user_id),
            message='Привет, я новый бот!',
            random_id=random.getrandbits(64)
        )

        return 'ok'

    return 'unsupported'
