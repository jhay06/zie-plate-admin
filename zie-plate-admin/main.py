from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/notification/user', methods=['POST','GET'])
def notificate_user():
    data = request.get_json()
    print(data)
    return jsonify(data)

@app.route('/auth/token_verify', methods=['POST'])
def token_verify():
    data = request.get_json()
    print(data)
    return jsonify(data)
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    print(data)
    return jsonify(data)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)