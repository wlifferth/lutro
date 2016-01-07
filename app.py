#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request


import crud



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST", "GET"])
def search():
    result = crud.look_up(request.form['query'])
    if result == None:
        return render_template("entry_not_found.html", word=request.form['query'])
    return render_template("entry.html", word=result.word, part_of_speech=result.part_of_speech, entry=result.definition)


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
