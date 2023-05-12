from flask import render_template, Blueprint
from pprint import pprint


from dao import dao_code

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="./templates")
posts = PostsDAO("./data/post.json", "./data/comments.json")


@main_blueprint.route("/")
def index_page():
    all_posts = posts.get_all_posts()
    pprint(all_posts)
    return render_template("index.html", posts=all_posts)
