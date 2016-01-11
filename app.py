#!/usr/bin/env python3
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for


import eng_crud
import esp_crud



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search/<string:query>", methods=["POST", "GET"], strict_slashes=False)
@app.route("/search", methods=["POST", "GET"], strict_slashes=False)
def search(query=None):
    if query == None:
        return redirect(url_for('index'))
    result = esp_crud.look_up(query)
    if result == None:
        result = eng_crud.look_up(query)
    if result == None:
        return render_template("entry_not_found.html", word=request.form['query'])
    return render_template("entry.html", word=result.word, part_of_speech=result.part_of_speech, entry=result.definition)


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
