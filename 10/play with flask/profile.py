from flask import Flask

app = Flask(__name__)

@app.route("/profile/")
def page_profile():
    return "Профиль пользователя"

app.run()