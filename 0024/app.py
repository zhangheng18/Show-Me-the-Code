# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask import render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#配置数据库信息
DATABASE = "todo.db"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////" + os.path.join(
    basedir, DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#数据库结构项
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    category_id = db.Column(
        db.Integer, db.ForeignKey('category.id'), default=1)


#构建数据库结构 类
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    items = db.relationship('Item', backref='category')


#初始化数据库，并添加测试数据
def init_db():
    """Insert default categories and demo items.
    """
    db.create_all()
    todo = Category(name=u'待完成')
    done = Category(name=u'已完成')

    item = Item(body=u'看一小时《战争与和平》')
    item2 = Item(body=u'浇花', category=todo)
    item3 = Item(body=u'收快递', category=done)

    db.session.add_all([todo, done, item, item2, item3])
    db.session.commit()


#首页
@app.route('/', methods=['GET', 'POST'])
def index():
    #第一次运行时初始化数据库
    if not os.path.exists(DATABASE): init_db()

    if request.method == 'POST':
        body = request.form.get('item')
        category_id = request.form.get('category')
        category = Category.query.get_or_404(category_id)
        item = Item(body=body, category=category)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('category', id=category_id))
    return redirect(url_for('category', id=1))


#分类页
@app.route('/category/<int:id>')
def category(id):
    category = Category.query.get_or_404(id)
    categories = Category.query.all()
    items = category.items
    return render_template(
        'index.html',
        items=items,
        categories=categories,
        category_now=category)


#编辑某项
@app.route('/edit-item/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    item = Item.query.get_or_404(id)
    category = item.category
    item.body = request.form.get('body')
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('category', id=category.id))


#添加到已完成
@app.route('/done/<int:id>', methods=['GET', 'POST'])
def done(id):
    item = Item.query.get_or_404(id)
    category = item.category
    done_category = Category.query.get_or_404(2)
    done_item = Item(body=item.body, category=done_category)
    db.session.add(done_item)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('category', id=category.id))


#删除某项
@app.route('/delete-item/<int:id>')
def del_item(id):
    item = Item.query.get_or_404(id)
    category = item.category
    if item is None:
        return redirect(url_for('category', id=1))
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('category', id=category.id))


if __name__ == '__main__':
    app.run(debug=True)
