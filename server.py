from flask import Flask, render_template, request, redirect, session, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.secret_key = 'shushmans'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test')
def test():
    test = {'hello': 'world'}
    return jsonify(test)
app.run(debug=True)
# {
#     'hats': [
#         {'title': 'a', 'price': '39', 'type': 'hat'},
#         {'title': 'b', 'price': '79', 'type': 'hat'},
#         {'title': 'c', 'price': '29', 'type', 'hat'}
#     ],
#     'shirts': [
#         {'title': 'a', 'price': '39', 'type': 'hat'},
#         {'title': 'b', 'price': '79', 'type': 'hat'},
#         {'title': 'c', 'price': '29', 'type', 'hat'}
#     ]
# }
