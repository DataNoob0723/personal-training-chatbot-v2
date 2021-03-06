# Import dependencies
from chatbot_core import ChatBot
from flask import Flask, jsonify, render_template, request
import json
import requests


app = Flask(__name__)

chatbot = ChatBot()

global response_dict
response_dict = {}


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route('/sendjson', methods=["POST"])
def sendjson():
    data = request.get_json(force=True)
    if data is not None:
        user_input = data["text"]
        bot_response = chatbot.generate_chat_response(user_input)
    else:
        bot_response = "Oops! Seems like that there is no data transfered from front end to back end!"
    response_dict["response"] = bot_response

    list_to_frontend = [response_dict, chatbot.info_dict]
    return jsonify(list_to_frontend)

            


if __name__ == "__main__":
    app.run(debug=True)