#sqlite3を使えるようにする
import sqlite3

from flask import Flask , render_template , request
#flaskのflask,render_templateを使用します宣言
app = Flask(__name__)

@app.route("/test")
def index():
    name = "flask"
    return render_template("test.html",name = name)

@app.route("/greet/<text>")
def hello(text):
    return text + "さん、こんにちは"

# @app.route("/sample/<text>")
# def school(school_name):
#     school_name = "oasa"
#     return render_template("test2.html",school_name = school_name)

@app.errorhandler(404)
def notfound(code):
    return "404ペーーーーージ"

#2日目データベースの接続
@app.route("/dbtest")
def dbtest():
    #データベースに接続
    conn = sqlite3.connect('flask.db')
    
    #どこのデータを抜くかコンソールを充てる。カーソル→目印
    c = conn.cursor()
    
    #execute:実行する
    c.execute("select name, adress from users where id=1")
    
    #fitchome:フェッチ:実際に所得する
    user_info=c.fetchone()
    
    #データベース接続終了
    c.close()
    
    #user_infoの中身を確認
    print(user_info)
    return render_template("dbtest.html", user_info = user_info)


#データベースを追加
@app.route("/add")
def add():
    return render_template("add.html")

#データを追加するボタンの処理
@app.route("/add",methods=["POST"])
def add_post():
    #add.htmlからfromのname="task"を取得
    task = request.form.get("task")
    #データベースに接続
    conn=sqlite3.connect("flask.db")
    c=conn.cursor()
    #(task,)のカンマは忘れずにね!ダブル型なので!
    #?に(task,)が入るよ
    #insert intoはデータを追加
    c.execute("insert into task values(null,?)",(task,))
    conn.commit()
    c.close()
    return "データを更新できました！"





#ここから上に記述する
if __name__ == "__main__":
    #サーバーを起動するよ
    app.run(debug=True)
    #デバックモードを有効にするよ