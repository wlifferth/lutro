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
    esp_result = esp_crud.look_up(query)
    eng_result = eng_crud.look_up(query)
    if esp_result == None and eng_result == None:
        return render_template("entry_not_found.html", word=request.form['query'])
    elif esp_result == None:
        return render_template("entry.html", word=eng_result.word, part_of_speech=eng_result.part_of_speech, entry=eng_result.definition)
    elif eng_result == None:
        return render_template("entry.html", word=esp_result.word, part_of_speech=esp_result.part_of_speech, entry=esp_result.definition)
    else:
        return render_template("two_entries.html", esp_word=esp_result.word, esp_part_of_speech=esp_result.part_of_speech, esp_entry=esp_result.definition, eng_word=eng_result.word, eng_part_of_speech=eng_result.part_of_speech, eng_entry=eng_result.definition)


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
