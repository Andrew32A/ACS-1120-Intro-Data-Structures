"""Main script, uses other modules to generate sentences."""
from flask import Flask
from sample import sentence_generator
from histogram import file_reader
from markov_chain import MarkovChain


app = Flask(__name__)

source_text_read = file_reader("./data/corpus.txt")
source_text_raw = "./data/corpus.txt"
markov = MarkovChain(source_text_read, source_text_raw)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = markov.generate_sentence()
    return sentence


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
