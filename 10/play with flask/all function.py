from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    return "Главная страничка"


@app.route("/profile/")
def page_profile():
    return "Профиль пользователя"


@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"


@app.route("/feed/")
def page_feed():
    return "Лента пользователя"

app.run()
