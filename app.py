import sys

from flask import Flask, render_template, jsonify, request, send_file
import aiapi

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)

app.register_error_handler(404, page_not_found)

messages = [{"role": "system", "content": ""}]

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        user_input = request.files['user_input']
        res = dict()

        res['answer'] = aiapi.generate_response(user_input, messages)
        res['answer'][0]
        return jsonify(res), 200


    return render_template('index.html', **locals())
