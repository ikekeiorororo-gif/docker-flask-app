from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Dockerized Python!"

@app.route('/about')
def about():
    app_version = "1.0.0"  # ここで動的に変数を作る
    return render_template('about.html', version=app_version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
