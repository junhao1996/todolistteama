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
    result = todo.read_all()

    return render_template('showall.html', list_todo=result)


@app.route('/delete/', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        a = request.form
        if a:
            print('aaa')
            b = request.form['warn']
            print(b)
            print(type(b))
            todo = todolistteamA()
            todo.delete(int(b))
            result = todo.read_all()
    return render_template('delete.html', list_todo=result)


@app.route('/show/')
def show():
    todo = todolistteamA()
    result = todo.read_maxone()
    print(result)
    return render_template('showlastone.html', res=result)


@app.route('/add/', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        print('post_______________________')
        a = request.form
        if a:
            b = request.form['content']
            print(b)
            c = request.form['warndate']
            print(c)
            todo = todolistteamA()
            todo.add1('dsd', b, c)
            # todo.read_all()
            result = todo.read_maxone()
            # return redirect('show')
        print('*' * 30)
        # ,addtodo = result
        return render_template('add.html')
    else:
        a = request.form
        if a:
            b = request.form['content']
            print(b)
            c = request.form['warndate']
            print(c)
            todo = todolistteamA()
            todo.add1('dsd', b, c)
            # todo.read_all()
            result = todo.read_maxone()
            # return redirect('show')
        print('*' * 30)
        # ,addtodo = result
        return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
#     saaaaaaaaaaaaaaaaaaaaaa

# @app.route('/add/', methods=['POST', 'GET'])
# def add():
#     if request.method == 'POST':
#         a = request.form['content']
#         print(a)
#         print('errot++++++++++++++++++++++++')
#     #
#     #
#     # else:
#     #     print('errot++++++++++++++++++++++++')
#
#     error = None
#
#     a = request.form
#     print(a)
#     if a:
#         b = request.form['content']
#         print(b)
#         c = request.form['warndate']
#         print(c)
#         todo = todolistteamA()
#         todo.add1('dsd', b, c)
#         # todo.read_all()
#         result = todo.read_maxone()
#     print('*'*30)
#     # ,addtodo = result
#     return render_template('add.html')
