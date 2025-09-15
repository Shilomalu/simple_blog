import sqlite3

# blog.dbという名前のデータベースに接続（ファイルがなければ新規作成される）
connection = sqlite3.connect('blog.db')

# SQLを実行するためのカーソルを取得
cursor = connection.cursor()

# postsテーブルを作成するSQL文
# id: 投稿番号 (自動で増える)
# title: タイトル (空であってはいけない)
# content: 内容 (空であってはいけない)
# created_at: 作成日時 (自動で記録される)
cursor.execute('''
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# 変更を確定
connection.commit()
# 接続を閉じる
connection.close()

print("データベースとテーブルが正常に作成されました。")