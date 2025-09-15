from flask import Flask, jsonify
from flask_cors import CORS  # 追加

app = Flask(__name__)
CORS(app)  # 追加

# ダミーの投稿データを作成します
dummy_posts = [
    {
        'id': 1,
        'title': 'Pythonからの最初の投稿',
        'content': 'これはバックエンド(Python)から取得した最初の投稿です！'
    },
    {
        'id': 2,
        'title': 'JSON形式について',
        'content': 'フロントエンドとバックエンドは、JSONという共通言語でデータを交換します。'
    }
]

# '/api/posts' というURLにアクセスがあった場合に、投稿データを返すAPI
@app.route('/api/posts')
def get_posts():
    return jsonify(dummy_posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)