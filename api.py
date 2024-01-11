from flask import Flask, Response
from main import genai_engine

app = Flask(__name__)


@app.route('/<query>')
def hello_world(query):
    return Response(genai_engine(query))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port =8123)