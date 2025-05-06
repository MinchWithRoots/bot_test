from flask import Flask, request
import json
import random
import vk_api

app = Flask(__name__)

# Данные для VK
confirmation_token = 'f52f1088'
token = 'vk1.a.69EGRWB1sbkT5O5nNF5WLcI9rsjx9_gDHPEcWWAQvL26fMZVkzKmoHM4fBNQMGjLhkQDAD-0NU16OALmxM_HmsyF0gDykLWuIjU1YV5ZlyWqQZD_r_8qTKp8NYsH8-04_9d9q1UA6IvBbj4_qd8a5o_F4Fr75eSGKWyw0x1kt1XfhW_W3GEaEC_u2Nt2lcH7kv7qo8wdQatf6BzohS5asA'

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

@app.route('/callback', methods=['POST'])
def processing():
    data = json.loads(request.data)

    if 'type' not in data:
        return 'not vk'

    if data['type'] == 'confirmation':
        return confirmation_token

    elif data['type'] == 'message_new':
        message = data['object']['message']
        user_id = message['from_id']
        text = message.get('text', '').lower()

        if text == 'начать' or text == '/start':
            send_message(user_id, "Привет! Нажми кнопку ниже, чтобы продолжить.", get_keyboard())
        elif text == 'команда1':
            send_message(user_id, "Ты выбрал первую команду!")
        elif text == 'команда2':
            send_message(user_id, "Ты выбрал вторую команду!")
        else:
            send_message(user_id, "Я тебя не понял. Напиши /start для начала.")

        return 'ok'

    return 'unsupported'

def send_message(user_id, message, keyboard=None):
    vk.messages.send(
        user_id=user_id,
        message=message,
        random_id=random.getrandbits(64),
        keyboard=keyboard
    )

def get_keyboard():
    keyboard = {
        "one_time": False,
        "buttons": [
            [{"action": {"type": "text", "label": "Команда1"}, "color": "primary"}],
            [{"action": {"type": "text", "label": "Команда2"}, "color": "secondary"}]
        ]
    }
    return json.dumps(keyboard, ensure_ascii=False)


