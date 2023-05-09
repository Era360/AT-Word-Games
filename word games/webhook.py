from flask import Flask, request, Response
from send_sms import SMS

app = Flask(__name__)

# TODO: create incoming messages route


@app.route('/incoming-messages', methods=['POST'])
def incoming_messages():
    data = request.get_json(force=True)
    print(f'Incoming message...\n ${data}')
    return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True)
