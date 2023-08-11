import hmac
import hashlib
import json
from flask import Flask
from flask import request

app = Flask(__name__)
app.config.from_json('config.json')

@app.route("/", methods=['GET', 'POST'])
def index():
    body = request.data
    signature = request.headers['x-pyrus-sig']
    secret = str.encode(app.config['SECRET_KEY'])

    if _is_signature_correct(body, secret, signature):
        return _prepare_response(body.decode('utf-8'))

def _is_signature_correct(message, secret, signature):
    digest = hmac.new(secret, msg=message, digestmod=hashlib.sha1).hexdigest()
    return hmac.compare_digest(digest, signature.lower())

def _prepare_response(body):
    task = json.loads(body)["task"]
    comment = task["comments"][-1]
    comment_author = comment["author"]
    author_name = comment_author["first_name"] + " " + comment_author["last_name"]
    comment_text = "Hello, {}! You said: {}".format(author_name, comment["text"])
    return "{{ \"text\":\"{}\", \"reassign_to\":{{ \"id\":{} }} }}".format(comment_text, comment_author["id"])

if __name__ == "__main__":
    app.run()
