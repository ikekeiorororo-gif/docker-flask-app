FROM python:3.12

WORKDIR /app

# 必要なライブラリを先にインストール
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# アプリとテンプレートをコピー
COPY app.py .
COPY templates/ templates/

# ポートを公開
EXPOSE 5000

# コンテナ起動時のコマンド
CMD ["python", "app.py"]


