import requests
from flask import Flask, render_template
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)
app = Flask(__name__)

@app.route('/joke')
def make_joke():
    params = { "limitTo": "nerdy" }
    r = requests.get("http://api.icndb.com/jokes/random", params=params)
    joke_json = r.json()
    joke_str = joke_json["value"]["joke"]
    return render_template("whatever.html", joke=joke_str)

if __name__ == "__main__":
    app.run()