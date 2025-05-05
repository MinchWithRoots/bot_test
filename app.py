from flask import Flask, request

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    data = request.json
    if data.get("type") == "confirmation":
        return "f52f1088"
    return "ok"

