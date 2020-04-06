# coding=gbk
from flask import Flask,request,url_for,render_template,redirect

app=Flask(__name__)
student=[["��֮��",'008',"����Ժ"],
     ["����",'005',"��ѧԺ"],
     ["����",'002',"�ƿ�Ժ"],
     ["�߷�",'003',"��ѧԺ"],
     [" ���� ",'001',"����Ժ"]]
def findnumber(Num):                                        #���ﶨ��һ������ѧ�ŵĺ��������㸴��
    for i in range(len(student)):
        if student[i][1]==Num:
            return i
    return -1

def save(stu):                                              #����һ������ĺ��������ı�����ʽ����Ϣ����
    studentfile=open('student.txt','w')
    for i in stu:
        for j in i:
            str=j
            studentfile.write(str)
            studentfile.write(' '*4)
        studentfile.write('\n')
    studentfile.close()

@app.route('/')                                            #�����Ǹ�Ŀ¼��Ҳ���Ǵ����ӵ�һ�����ʵ�ҳ��
def index():
    save(student)
    return render_template('index.html',student=student)   #�����student=student���Ⱥ������Ҫ����html�ļ��ı������ұ������涨��Ķ�ά�б�

@app.route('/delstu',methods=['GET','POST'])               #������ɾ��ģ�飬��Ӧ��ҳ����/delstu
def delstu():
    if request.method=='POST':
        delnumber = request.form.get('delnumber')
        if findnumber(delnumber)==-1:
            return '�������ѧ�Ų�����'
        else:
            del student[findnumber(delnumber)]
            save(student)
            return redirect(url_for('index'))              #����ҵ��������ѧ��ִ��ɾ�����������ض�����ҳ
    return render_template('delstu.html',student=student)

@app.route('/addstu',methods=['GET','POST'])               #���������ģ��
def addstu():
    if request.method=='POST':
        addnumber = request.form.get('addnumber')
        if findnumber(addnumber)!=-1:
            return "�������ѧ���Ѵ���"
        else:
            addname = request.form.get('addname')
            adddepartment = request.form.get('adddepartment')
            if addname != None and adddepartment and addnumber != None:            #��Ϊ�������
                student.append([addname, addnumber, adddepartment])
                save(student)
                return redirect(url_for('index'))
    return render_template('addstu.html')                     #��ӳɹ����ض�����ҳ

@app.route('/altstu',methods=['GET','POST'])                  #�������޸�ģ�飬��Ҫ�ҵ�Ҫ�޸ĵ�ѧ�ţ�����ҵ��˽��в���
def altstu():
    if request.method=='POST':
        altnumber = request.form.get('altnumber')
        altdep = request.form.get('altdepartment')
        altname = request.form.get('altname')
        if findnumber(altnumber)==-1:
            return '�������ѧ�Ų�����'
        else:
                if altdep !='':                              #�����һ�Ե�������ʲô��û�У���ʾ����������Ϊ�գ��������޸�
                    student[findnumber(altdep)][2]=altdep
                if altname!='':
                    student[findnumber(altname)][0]=altname
                    save(student)
                return render_template('index.html', student=student)


    return render_template('altstu.html')

@app.route('/searchstu',methods=['GET','POST'])
def searchstu():
    if request.method=='POST':
        number = request.form.get('number')
        if findnumber(number)==-1:
            return 'û����Ҫ�ҵ�ѧ��'
        else:
            find=student[findnumber(number)]
            return render_template('searchstu.html',find=find)      #����ҵ���ѧ�ţ��Ѹ�ѧ����Ϣ����html
    return render_template('searchstu.html',student=student)

if __name__ == '__main__':
    app.run(debug=True)

