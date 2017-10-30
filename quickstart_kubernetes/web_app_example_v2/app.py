from flask import Flask, jsonify
import requests
import logging
import os

app = Flask(__name__)

# Set the Go API environmental variables
GO_API_HOST = os.getenv("GO_API_SERVICE_HOST", None)
GO_API_PORT = os.getenv("GO_API_SERVICE_PORT", None)

assert GO_API_PORT is not None, "Did not find the Go API port environment variable"
assert GO_API_HOST is not None, "Did not find the Go API host environment variable"


# Set logs to info level
logging.basicConfig(level=logging.INFO)


@app.route("/")
def hello_world():
	"""
		Returns hello world as a response
	"""
	logging.info("Enter Hello World Route")
	return "Hello World"

@app.route("/api_call")
def api_call():
	"""
		Calls the Go API which then returns a JSON accordingly
	"""
	logging.info("Enter Api Call Route")
	url = "http://%s:%s/api/person/v1/0010" % (GO_API_HOST, GO_API_PORT)
	data = requests.get(url)
	data = data.json()
	return jsonify(data)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8080")


