from flask import Flask, render_template, request
from utils.unsplash import get_photos

app = Flask(__name__)

CATEGORIES = ["nature", "technology", "food", "travel", "people"]

@app.route("/", methods=["GET", "POST"])
def home():
    images = []
    if request.method == "POST":
        query = request.form.get("query")
        images = get_photos(query)
    return render_template("index.html", images=images, categories=CATEGORIES)

@app.route("/category/<name>")
def show_category(name):   # unique function name
    images = get_photos(name)
    return render_template("gallery.html", images=images, categories=CATEGORIES)

if __name__ == "__main__":
    app.run(debug=True)
