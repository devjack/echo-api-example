from flask import Flask, request, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        'code': '404',
        'message': "URL not found"
    }), 404

@app.route("/echo")
def hello():
    echo = request.args.get('echo')
    response = {
        'hello': 'world',
        'echo' : echo or ''
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)
