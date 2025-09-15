# Flaskというフレームワークから、Flaskクラスをインポートします
from flask import Flask

# Flaskクラスのインスタンス（実体）を作成します
app = Flask(__name__)

# ルーティングを設定します。'/'へのアクセスがあった場合に、以下の関数が実行されます
@app.route('/')
def hello():
    # ブラウザに表示する文字列を返します
    return 'Hello from Python Backend!'

# このファイルが直接実行された場合に、Webサーバーを起動します
if __name__ == '__main__':
    # host='0.0.0.0'は、どのネットワークからでもアクセス可能にする設定です
    # port=5000は、5000番ポートで待ち受ける設定です
    app.run(host='0.0.0.0', port=5000, debug=True)