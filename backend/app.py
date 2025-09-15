# requestを追加でインポートします
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

dummy_posts = [
    # ... (今までのダミーデータはそのまま) ...
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

# '/api/posts' へのGETリクエスト（データ取得）とPOSTリクエスト（データ作成）の両方を受け付けるようにします
@app.route('/api/posts', methods=['GET', 'POST'])
def handle_posts():
    # POSTリクエストの場合（新しい投稿を作成）
    if request.method == 'POST':
        # フロントエンドから送られてきたJSONデータを取得します
        data = request.get_json()
        
        # 新しい投稿データを作成します
        new_post = {
            'id': len(dummy_posts) + 1,
            'title': data['title'],
            'content': data['content']
        }
        # dummy_postsリストに新しい投稿を追加します
        dummy_posts.append(new_post)
        
        # 追加した投稿データをフロントエンドに返します
        return jsonify(new_post), 201 # 201は「作成成功」を意味するステータスコードです
    
    # GETリクエストの場合（投稿一覧を取得）
    else:
        return jsonify(dummy_posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)