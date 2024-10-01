from flask import Flask, request

app = Flask(__name__)

# ルートエンドポイント
@app.route('/')
def home():
    return 'Flaskサーバが稼働しています。'

# リダイレクトURLとして使用されるエンドポイント
@app.route('/callback')
def callback():
    # Patreonからのリダイレクトで渡されるクエリパラメータ（例: 認可コード）
    code = request.args.get('code')
    if code:
        return f'認可コードを受け取りました: {code}'
    else:
        return '認可コードが含まれていません。'

if __name__ == '__main__':
    app.run(debug=True)
