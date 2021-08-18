from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

from app import app  # 从app包中导入 app这个实例


# 2个路由
@app.route('/')
@app.route('/index')
# 1个视图函数
def index():
    user = {'username': '朱世维'}
    # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()  # 表单实例化对象
    if login_form.validate_on_submit():
        flash('Login requested for user {},remember_me={}'.format(login_form.username.data, login_form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=login_form)
