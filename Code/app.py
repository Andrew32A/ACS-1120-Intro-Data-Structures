"""Main script, uses other modules to generate sentences."""
from flask import Flask
from sample import sentence_generator
from histogram import file_reader


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    source_text = file_reader("./data/corpus.txt")
    sentence = sentence_generator(source_text, 10)
    return sentence


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
