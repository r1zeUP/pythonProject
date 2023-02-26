from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)


@app.route("/mastatic/<path:path>")
def static_dir(path):
    return send_from_directory("mastatic", path)


app.run()
