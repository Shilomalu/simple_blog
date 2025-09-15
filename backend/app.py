import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# データベースに接続して、結果を辞書のリストとして返すためのヘルパー関数
def get_db_connection():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row # 列名でアクセスできるようにする
    return conn

# '/api/posts' へのGETリクエスト（データ取得）とPOSTリクエスト（データ作成）
@app.route('/api/posts', methods=['GET', 'POST'])
def handle_posts():
    conn = get_db_connection()
    
    # POSTリクエストの場合（新しい投稿を作成）
    if request.method == 'POST':
        data = request.get_json()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                     (data['title'], data['content']))
        conn.commit()
        conn.close()
        return jsonify({'status': 'success'}), 201

    # GETリクエストの場合（投稿一覧を取得）
    else:
        posts_query = conn.execute('SELECT * FROM posts ORDER BY created_at DESC').fetchall()
        conn.close()
        
        # データベースの結果を辞書のリストに変換
        posts = [dict(row) for row in posts_query]
        return jsonify(posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)