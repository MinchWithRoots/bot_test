from flask import Flask, request, json
from settings import *
import vk
import random

app = Flask(__name__)

@app.route('/', methods=['POST'])
def processing():
    #Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    #Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v='5.110')
        user_id = data['object']['message']['from_id']
        api.messages.send(access_token=token, user_id=str(user_id), message='Привет, я новый бот!', random_id=random.getrandbits(64))
        # Сообщение о том, что обработка прошла успешно
        return 'ok'
