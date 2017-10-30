from flask import Flask
import logging

app = Flask(__name__)

# Set logs to info level
logging.basicConfig(level=logging.INFO)

# Set logs to info level
logging.basicConfig(level=logging.INFO)

@app.route("/")
def hello_world():
	"""
		Returns hello world as a response
	"""
	logging.info("Enter Hello World Route")
	return "Hello World"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8080")