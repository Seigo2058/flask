#sqlite3を使えるようにする
import sqlite3

from flask import Flask , render_template , request , redirect
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
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    #(task,)のカンマは忘れずにね!ダブル型なので!
    #?に(task,)が入るよ
    #insert intoはデータを追加
    c.execute("insert into task values(null,?)",(task,))
    conn.commit()
    c.close()
    return "データを更新できました！"

#3日目 listを表示

@app.route("/list")
def task_list():
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    c.execute("select id ,task from task ")
    task_list = []
    for row in c.fetchall():
        task_list.append({"id":row[0], "task":row[1]})
    c.close()
    return render_template("list.html" , task_list = task_list)

#データベースを消す変更を加える

@app.route("/del/<int:id>")
def del_list(id):
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    c.execute("delete from task where id =?",(id,))
    conn.commit()
    conn.close()
    return redirect("list")

#編集機能(update)

@app.route("/edit/<int:id>")
def edit(id):
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    c.execute("select id ,task from task where  id = ?",(id,))
    task = c.fetchone()
    conn.close()
    task = task[0]
    item = {"id":id,"task":task}
    return render_template("/edit.html",task = item)

@app.route("/edit" , methods = ["POSt"])
def update_task():
    item_id = request.form.get("task_id")
    item_id = int(item_id)
    task = request.form.get("task")
    conn = sqlite3.connect("flask.db")
    c = conn.cursor()
    c.execute("update task set task = ? where id = ?",(task , item_id))
    task = c.fetchone()
    conn.close()
    return render_template("/list")





#ここから上に記述する
if __name__ == "__main__":
    #サーバーを起動するよ
    app.run(debug=True)
    #デバックモードを有効にするよ