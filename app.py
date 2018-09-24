import flask

app = flask.Flask(__name__)

@app.route('/v1/austinThunderstorms')
def austin_thunderstorms():
    return flask.jsonify({
        'areThereThunderstorms': True,
    })
