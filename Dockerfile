# ベースイメージとしてSeleniumのChromiumを使用
FROM selenium/standalone-chromium:latest

# rootユーザーに切り替える
USER root

# Pythonの仮想環境用ツールをインストール
RUN apt-get update && apt-get install -y python3-venv

# 仮想環境を作成
RUN python3 -m venv /usr/src/app/venv

# 仮想環境を有効化してpipをインストール
RUN /usr/src/app/venv/bin/pip install --upgrade pip

# Seleniumをインストール
RUN /usr/src/app/venv/bin/pip install selenium

# Chromium用のWebDriverをダウンロード（必要に応じてバージョン指定）
RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip -P /tmp \
    && unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin \
    && rm /tmp/chromedriver_linux64.zip

# 自作のPythonファイルをコンテナ内にコピー
COPY . /usr/src/app/

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# コンテナ起動時にPythonファイルを実行
CMD ["python3", "get_selenium.py"]
