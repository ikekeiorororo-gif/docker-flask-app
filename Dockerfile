FROM python:3.12

# 必要なライブラリを先にインストール
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000


# アプリとテンプレートをコピー
COPY app.py .
COPY templates/ templates/
COPY . .               # これでプロジェクト全体をコピー
COPY .env .env         # 明示的に.envだけをコピーする場合

CMD ["python", "app.py"]
# コンテナ起動時のコマンド
CMD ["python", "app.py"]

