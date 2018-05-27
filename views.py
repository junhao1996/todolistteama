from flask import Flask,make_response,redirect,abort
from flask import  render_template


app = Flask(__name__)        #创建一个wsgi应用
@app.route('/')
def index():
    return "hello,world!"
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

#
@app.route('/login')             #添加路由：根
def login():
    return render_template('login.html')




@app.route('/showall/')
def showall(name=None):
    return render_template('showall.html', name=name)

@app.route('/redir')
def redir():
    return redirect('https://www.baidu.com')





if __name__ == '__main__':
    app.run(debug=True)