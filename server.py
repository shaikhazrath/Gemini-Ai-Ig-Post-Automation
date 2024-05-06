from flask import Flask
from main import create_quote_post
app = Flask(__name__)

@app.route('/')
def hello():
    create_quote_post()
    return "posted"

if __name__ == '__main__':
    app.run(debug=True)
