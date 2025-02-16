FROM python:3.11-slim

WORKDIR /app

# システムパッケージをインストール
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 仮想環境を作成
RUN python3 -m venv /venv

# 仮想環境にpipをインストール
RUN /venv/bin/pip install --upgrade pip

# requirements.txtをコピーしてパッケージをインストール
COPY requirements.txt /app/requirements.txt
RUN /venv/bin/pip install -r /app/requirements.txt

# ポートを開放
EXPOSE 4444

# 仮想環境を有効にしてスクリプトを実行するエントリポイント
CMD ["/venv/bin/python", "get_selenium.py"]