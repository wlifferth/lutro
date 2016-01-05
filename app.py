#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request


from esperanto import look_up


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST", "GET"])
def search():
    query = request.form['query']
    result = look_up(query)
    return render_template("entry.html", word=result.word, entry=result.entry)


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
