FROM python:3.12

# 必要なライブラリを先にインストール
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

#EXPOSE 5000


# アプリとテンプレートをコピー
COPY app.py .
COPY templates/ templates/

# コンテナ起動時のコマンド
CMD ["python", "app.py"]

