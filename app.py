from flask import Flask, request
import json
import random
import vk

app = Flask(__name__)

# Токены из настроек твоей группы
confirmation_token = 'f52f1088'  # Токен для подтверждения от VK
token = 'vk1.a.69EGRWB1sbkT5O5nNF5WLcI9rsjx9_gDHPEcWWAQvL26fMZVkzKmoHM4fBNQMGjLhkQDAD-0NU16OALmxM_HmsyF0gDykLWuIjU1YV5ZlyWqQZD_r_8qTKp8NYsH8-04_9d9q1UA6IvBbj4_qd8a5o_F4Fr75eSGKWyw0x1kt1XfhW_W3GEaEC_u2Nt2lcH7kv7qo8wdQatf6BzohS5asA'       # Токен для отправки сообщений

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
