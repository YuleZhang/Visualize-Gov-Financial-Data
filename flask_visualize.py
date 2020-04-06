'''
@Author: YuleZhang
@Description: 
@Date: 2020-04-01 20:10:50
'''
# encoding = utf-8
from flask import Flask,render_template,redirect,url_for,request,jsonify
from database import Database

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('index.html')

@app.route('/regist',methods=['GET','POST'])
def regist():
    # 账号注册
    return render_template('register.html')

@app.route('/admin',methods=['GET','POST'])
def admin():
    # 管理员界面
    if request.method=='POST':
        db = Database()
        result = db.search_file()
        return render_template('admin.html',result = result)
    return render_template('admin.html')

@app.route('/search',methods=['GET','POST'])
def search():
    # 查询用户信息
    db = Database()
    fileType = request.form['type']
    year = request.form['year']
    result = db.search_file_cond(fileType,year)
    return jsonify(result)

@app.route('/addUser',methods=['GET','POST'])
def addUser():
    # 添加用户信息
    db = Database()
    if request.method=='POST':
        user = request.form['user']
        password = request.form['password']
        db.insert_user(user, password)
        result = db.search_user()
        return jsonify(result)
    result = db.search_user()
    return render_template("userManagement.html",result=result)


@app.route('/deleteUser',methods=['GET','POST'])
def delete():
    # 删除用户信息
    db = Database()
    if request.method=='POST':
        user = request.form['user']
        db.delete_user(user)
        result = db.search_user()
        return jsonify(result)
    return jsonify("{}")


@app.route('/modifyUser',methods=['GET','POST'])
def modify():
    # 修改用户信息
    db = Database()
    if request.method=='POST':
        user = request.form['user']
        password = request.form['password']
        db.modify_user(user,password)
        result = db.search_user()
        return jsonify(result)
    return jsonify("{}")


@app.route('/improveLevel',methods=['GET','POST'])
def improveLevel():
    # 提升user权限
    db = Database()
    if request.method=='POST':
        user = request.form['user']
        db.improve_user(user)
        result = db.search_user()
        return jsonify(result)
    return jsonify("{}")

if __name__ == "__main__":
    app.run(threaded=True)
    
