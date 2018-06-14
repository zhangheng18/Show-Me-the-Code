import sqlite3, os
from datetime import datetime

from flask import Flask
from flask import render_template, request, redirect
from flask import g

DATABASE = "guestbook.db"

app = Flask(__name__)


#绑定数据库链接
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


#第一次初始化数据库结构
def init_db():
    db = get_db()
    db.cursor().execute("""CREATE TABLE GUESTBOOK(
    USERNAME TEXT NOT NULL,
    COMMENT TEXT NOT NULL,
    CREATEAT TEXT NOT NULL);
    """)
    db.commit()


#加载留言
def load_data():
    cur = get_db().execute("SELECT * from GUESTBOOK")
    rv = cur.fetchall()
    cur.close()

    return rv


#保存留言
def save_data(name, comment, create_at):
    db = get_db()
    cur = db.cursor().execute(
        "INSERT INTO GUESTBOOK (USERNAME,COMMENT,CREATEAT) VALUES (?,?,?)",
        (name, comment, create_at))
    cur.close()
    db.commit()


#响应主页
@app.route('/')
def index():

    #第一次运行时初始化数据库
    if not os.path.exists(DATABASE): init_db()

    #获取留言数据
    greeting_list = load_data()
    #渲染html页面
    return render_template('index.html', greeting_list=greeting_list)


#得到POST方法提交的表单数据。
@app.route('/post', methods=['POST'])
def post():
    name = request.form['name']
    comment = request.form['comment']
    create_at = datetime.now()

    save_data(name, comment, create_at)

    return redirect('/')


if __name__ == '__main__':
    app.run('127.0.0.1', port='5000', debug=True)
