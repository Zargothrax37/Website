from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/2")
def home2():
    return render_template("blog-list.html")


@app.route("/3")
def home3():
    return render_template("blog-post.html")


if __name__ == "__main__":
    app.run(debug=True)
