import sqlite3
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from register import models


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        models.UserInfo.objects.create(name=name, email=email, pwd=pwd)
        messages.success(request, "账号创建成功")
        # return HttpResponseRedirect('../login')
    return render(request, 'register/index.html')

# def register_in(namein, emailin, pwdin):
#     print(type(namein))
#     print(emailin)
#     print(pwdin)
# con = sqlite3.connect('../db.sqlite3')
# cur = con.cursor()
# # 编写sql语句
# sql = 'insert into register_userinfo(name,email,pwd) values(?,?,?)'  # 括号中是插入的字段，用逗号隔开，values中是插入的值，问好为占位符
# # 执行sql
# try:
#     cur.execute(sql, (str(namein), str(emailin), str(pwdin)))  # 插入一条数据
#     # cur.executemany(sql, [('张三', 28),('李四'，30),('王五'，27)])  # 插入多条
#     # 提交事务
#     con.commit()
#     print("创建账号成功")
# except Exception as e:
#     print(e)
#     con.rollback()
#     print("创建账号失败")
# finally:
#     cur.close()
#     con.close()


# register_in("CFT", "1204551784@qq.com", "123456")
