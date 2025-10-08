from flask import Flask, render_template, request
import requests
import os

from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

#HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/gpt2"
HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/distilgpt2"
HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

@app.route('/')
def hello():
    return "Hello from Dockerized Python3 ryomo!"

@app.route('/huggingface', methods=['GET', 'POST'])
def huggingface():
    answer = ""
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = requests.post(HUGGINGFACE_API_URL, headers=headers, json={"inputs": prompt})
        if response.status_code == 200:
            # Hugging Face API の返却形式によって変更が必要
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
    key = os.environ.get("HUGGINGFACE_API_KEY")
    if key:
        return "HUGGINGFACE_API_KEY is set ✅"
    else:
        return "HUGGINGFACE_API_KEY is NOT set ❌"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Renderが指定するPORTを取得
    app.run(host="0.0.0.0", port=port)
