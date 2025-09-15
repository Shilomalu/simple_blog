document.addEventListener('DOMContentLoaded', () => {
    const postList = document.querySelector('.post-list');
    const postForm = document.querySelector('.post-form form');

    // 投稿データを取得して表示する関数
    const fetchPosts = () => {
        fetch('http://127.0.0.1:5000/api/posts')
            .then(response => response.json())
            .then(posts => {
                postList.innerHTML = '<h2>投稿一覧</h2>';
                posts.forEach(post => {
                    const article = document.createElement('article');
                    article.innerHTML = `
                        <h3>${post.title}</h3>
                        <p>${post.content}</p>
                    `;
                    postList.appendChild(article);
                });
            })
            .catch(error => console.error('データの取得に失敗しました:', error));
    };

    // フォームが送信されたときの処理
    postForm.addEventListener('submit', (e) => {
        e.preventDefault(); // フォームのデフォルトの送信動作（ページリロード）を防ぎます

        // フォームからタイトルと内容を取得します
        const title = document.getElementById('title').value;
        const content = document.getElementById('content').value;

        // バックエンドにPOSTリクエストで新しい投稿データを送信します
        fetch('http://127.0.0.1:5000/api/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ title: title, content: content }), // JavaScriptオブジェクトをJSON文字列に変換します
        })
        .then(response => response.json())
        .then(newPost => {
            console.log('新しい投稿が追加されました:', newPost);
            // 投稿フォームを空にします
            postForm.reset();
            // 投稿一覧を再読み込みして、新しい投稿を画面に反映させます
            fetchPosts();
        })
        .catch(error => console.error('投稿に失敗しました:', error));
    });

    // 最初にページが読み込まれたときに投稿一覧を取得します
    fetchPosts();
});