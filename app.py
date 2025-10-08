from flask import Flask, render_template, request
import requests
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

#てすと見るだけ
API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
API_KEY = os.environ.get("HUGGINGFACE_API_KEY")
headers = {"Authorization": f"Bearer {API_KEY}"}

response = requests.post(API_URL, headers=headers, json={"inputs": "Hello world"})
print(response.status_code)
print(response.json())


# 無料で使えるモデル URL に変更
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}





@app.route('/')
def hello():
    return "Hello from Render + Docker Flas1!"

@app.route('/huggingface', methods=['GET', 'POST'])
def huggingface():
    answer = ""
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = requests.post(HUGGINGFACE_API_URL, headers=headers, json={"inputs": prompt})
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list):
                answer = result[0]["generated_text"]
            else:
                answer = str(result)
        else:
            answer = f"Error: {response.status_code}"
    return render_template('huggingface.html', answer=answer)

@app.route("/check_env")
def check_env():
    if HUGGINGFACE_API_KEY:
        return "HUGGINGFACE_API_KEY is set ✅"
    else:
        return "HUGGINGFACE_API_KEY is NOT set ❌"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
