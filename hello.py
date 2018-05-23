from flask import Flask, render_template, request, redirect, url_for
import random


app = Flask(__name__)
ms = [
    "あなたの名前を教えて下さい",
    "あなたの名前は何ですか？",
    "名前を入力してね"
]

@app.route('/')
def index():
    title = 'ようこそ'
    message = random.choice(ms)
    #index.htmlをレンダリング
    return render_template('index.html', message=message, title=title)


@app.route('/post', methods=['GET','POST'])
def post():
    title = 'こんにちは！'
    #HTTPメソッドがpostだったら
    if request.method == 'POST':
        name = request.form['name']
        return render_template('index.html', name=name, title=title)
    else:
        #エラった場合のリダイレクト
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()