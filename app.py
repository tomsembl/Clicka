from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8, debug=True)