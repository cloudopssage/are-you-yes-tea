from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
BASE_URL = "http://127.0.0.1:8080/books"

@app.route("/")
def index():
    response = requests.get(BASE_URL)
    books = response.json() if response.status_code == 200 else []
    return render_template("index.html", books=books)

@app.route("/add", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    new_book = {"id": len(requests.get(BASE_URL).json()) + 1, "title": title, "author": author}
    requests.post(BASE_URL, json=new_book)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
