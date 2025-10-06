from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Dockerized Python!"

@app.route('/about')
def about():
    return render_template('about.html')  # ← ここを変更

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
