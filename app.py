from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from suz Flask in Docker!"

@app.route('/about')
def about():
    return "This is the About page of my suz Flask app."

if __name__ == "__main__":
    # host="0.0.0.0" でコンテナ外からアクセス可能にする
    app.run(host="0.0.0.0", port=5000)
