from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

# OpenAI クライアント作成
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
print("OPENAI_API_KEY:", OPENAI_API_KEY)  # コンテナログで確認
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    prompt = ""
    answer = ""
    if request.method == 'POST':
        prompt = request.form.get('prompt', '')
        if prompt:
            try:
                response = client.chat.completions.create(
                    model="gpt-4.1",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=500
                )
                # 新しい SDK では message はオブジェクトなので .content で取得
                answer = response.choices[0].message.content
            except Exception as e:
                answer = f"Error: {str(e)}"
        else:
            answer = "プロンプトを入力してください。"

    return render_template('about.html', answer=answer, prompt=prompt)

@app.route("/check_env")
def check_env():
    if OPENAI_API_KEY:
        return "OPENAI_API_KEY is set ✅"
    else:
        return "OPENAI_API_KEY is NOT set ❌"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
