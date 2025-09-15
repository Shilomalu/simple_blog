// ページが読み込まれたときに、以下の処理を実行します
document.addEventListener('DOMContentLoaded', () => {
    // 投稿一覧を表示する要素を取得します
    const postList = document.querySelector('.post-list');

    // バックエンドのAPIにリクエストを送信して、投稿データを取得します
    fetch('http://127.0.0.1:5000/api/posts')
        .then(response => response.json()) // 受け取ったデータをJSONとして解釈します
        .then(posts => {
            // 最初に表示されているダミーの投稿を空にします
            postList.innerHTML = '<h2>投稿一覧</h2>';
            
            // 取得した投稿データの一つひとつに対して、HTML要素を作成して追加します
            posts.forEach(post => {
                const article = document.createElement('article');
                article.innerHTML = `
                    <h3>${post.title}</h3>
                    <p>${post.content}</p>
                `;
                postList.appendChild(article);
            });
        })
        .catch(error => {
            // もしエラーが発生したら、コンソールに表示します
            console.error('データの取得に失敗しました:', error);
        });
});