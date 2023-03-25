import io
import sys
import pickle
import base64
import pickletools

import secret

from flask import Flask, request, render_template


black_func = ['tuple', 'map', 'eval', 'exec', 'open', '__import__', 'exit', 'input', 'globals', 'getattr', 'dict']
black_char = ['\'', '"', 'R', 'p', 'o', 'i', 'S']


key = 'vyBNg1o5n37eWwPR'


app = Flask(__name__)


class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self,module, name):
        if module in black_func or name in black_func:
            return "hacker"
        if isinstance(module, str):
            return getattr(sys.modules[module], name)
        else:
            return getattr(module, name)


def restricted_loads(s):
    for i in pickletools.genops(s):
        opcode = repr(i[0].code)[1:-1]
        if opcode in black_char:
            return "hacker"
    return RestrictedUnpickler(io.BytesIO(s)).load()


@app.route('/', methods=['GET'])
def index():
    return "emmmm, nothing here.<br>maybe u could go to /nohacker"


@app.route('/nohacker', methods=['GET', 'POST'])
def nohacker():
    if not request.form.get('m'):
        return 'where\'s ur message?'
    m = base64.b64decode(request.form.get('m'))
    load = restricted_loads(m)
    if load:
        return load
    if key != secret.secretKey:
        return 'wrong key'
    else:
        return 'WoW, you really know hacking'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

