import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Testdata for the API
programming = [
    {'id': 0,
     'title': 'C#',
     'text': '.NET programming',},
    {'id': 1,
     'title': 'Python',
     'text': 'AI and ML',},
    {'id': 2,
     'title': 'PHP',
     'text': 'For my homepage',}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Sample JSON api</h1>'''


@app.route('/api/v1/resources/programming/all', methods=['GET'])
def api_all():
    return jsonify(programming)


@app.route('/api/v1/resources/programming', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: You need to enter a valid id."

    # An empty list to append result
    result = []

    for prog in programming:
        if prog['id'] == id:
            results.append(prog)


    return jsonify(result)

@app.route('/api/v1/resources/programming/<uuid>', methods=['GET', 'POST'])
def add_lang(uuid):
    content = request.json
    programming.append(content)
    return jsonify({"id":uuid})

app.run()