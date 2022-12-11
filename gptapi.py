from flask import Flask, jsonify, request
from pyChatGPT import ChatGPT
def func(msgs):
	session_token = ''  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
	api = ChatGPT(session_token)  # auth with session token
	resp = api.send_message(msgs)
	api.refresh_auth()  # refresh the authorization token
	api.reset_conversation()
	print(resp['message'])
	return resp['message']

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def home():
	print(request.args.get('data'))
	msgs = func(request.args.get('data'))
	return jsonify({
        'status': 200,
        'data': msgs
		    })

if __name__ == '__main__':
    app.run()




