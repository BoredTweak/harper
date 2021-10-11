import time
import json
from techharper import GitHubService
from flask import Flask, request

""" Module that monkey-patches json module when it's imported so
JSONEncoder.default() automatically checks for a special "to_json()"
method and uses it to encode the object if found.

Credit: https://stackoverflow.com/questions/18478287/making-object-json-serializable-with-regular-encoder/18561055#18561055
"""
from json import JSONEncoder

def _default(self, obj):
    return getattr(obj.__class__, "to_json", _default.default)(obj)

_default.default = JSONEncoder.default  # Save unmodified default.
JSONEncoder.default = _default # Replace it.

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/tech')
def tech():
    repo = request.args.get('repo')
    token = request.headers.get('token')
    service = GitHubService(token)
    output = service.generateNotification(repo)
    results = json.dumps([output], indent = 4)
    return results


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)