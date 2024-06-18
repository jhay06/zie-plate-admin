from flask import Flask, request, jsonify
from threading import Thread
import requests

app = Flask(__name__)


def create_app():
    t = Thread(target=stay_alive)
    t.start()
    return app

def stay_alive():
    from time import sleep
    while True:
        print('Stay Alive')
        requests.get('https://zie-plate-admin.glitch.me')
        sleep(60 * 2)


@app.route('/webhook/page', methods=['POST', 'GET'])
def notification_page():
    from app_code.page_controller import PageController
    if request.method == 'GET':
        try:
            hub_mode = request.args.get('hub.mode')
            if hub_mode == 'subscribe':
                subscription_query = request.args
                page_controller = PageController()
                return page_controller.subscribe(subscription_query)
            else:
                return 'Invalid'
        except Exception as e:
            return 'Invalid'
    if request.method == 'POST':
        try:
            post_query = request.get_json()
            page_controller = PageController()
            return page_controller.process(post_query)
        except Exception as e:
            return 'Invalid'


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

