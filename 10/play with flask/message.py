from flask import Flask

app = Flask(__name__)

@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"

app.run()