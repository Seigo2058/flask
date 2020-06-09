from flask import Flask , render_template
#flaskのflask,render_templateを使用します宣言
app = Flask(__name__)

@app.route("/test")
def index():
    name = "flask"
    return render_template("test.html",name = name)

@app.route("/greet/<text>")
def hello(text):
    return text + "さん、こんにちは"

@app.route("/sample/<text>")
def scholl(school_name):
    return "学校名は"+ school_name + "です"


if __name__ == "__main__":
    #サーバーを起動するよ
    app.run(debug=True)
    #デバックモードを有効にするよ