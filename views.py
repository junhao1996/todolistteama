from flask import Flask, make_response, redirect, abort, request
from flask import render_template

from todo import todolistteamA

app = Flask(__name__)  # 创建一个wsgi应用


@app.route('/')
def index():
    return "hello,world!"


# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

#
@app.route('/login')  # 添加路由：根
def login():
    return render_template('login.html')


@app.route('/showall/')
@app.route('/showall/<name>')
def showall(name=None):
    todo = todolistteamA()
    result= todo.readAll()


    return render_template('showall.html', list_todo = result)



@app.route('/redir')
def redir():
    return redirect('https://www.baidu.com')


@app.route('/add/', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        a = request.form['content']
        print(a)


    else:
        print('errot++++++++++++++++++++++++')

    error = None

    a = request.form
    print(a)
    if a:
        b = request.form['content']
        print(b)
        c = request.form['warndate']
        print(c)
        todo = todolistteamA()
        todo.add1('dsd', b, c)
        todo.readAll()
    print('*'*30)
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
