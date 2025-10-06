FROM python:3.12

# 必要なライブラリを先にインストール
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

# アプリをコピー
COPY app.py .

# コンテナ起動時に Flask を実行
CMD ["python", "app.py"]
