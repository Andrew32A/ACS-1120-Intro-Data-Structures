"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from markov_chain import MarkovChain


app = Flask(__name__)

source_text = "./data/shrek_corpus.txt"
markov = MarkovChain(source_text)
max_words = 10

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = markov.generate_sentence(max_words)

    context = {
        "sentence": sentence
    }

    return render_template("index.html", **context)

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
