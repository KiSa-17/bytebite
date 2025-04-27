import mysql.connector as bb
mycon=bb.connect(host="localhost", user='root', passwd='9302oppo',database='mycare')
if mycon.is_connected():
    print('Welcome to mycare')
cursor=mycon.cursor()
def newuser(name,pwrd,ty):
    cursor.execute("insert into users (id,username,type,password) values(%s,%s,%s)",(null,name,ty,pwrd))
    mycon.commit()
    cursor.close()
    mycon.close()
def getuser(uid):
    cursor.execute("select * from users where id =%s",(uid))
    user= cursor.fetchone()
    cursor.close()
    mycon.close()
    return user
def new_med_detail(mname,man,exp):
    cursor.execute("insert into medicine(mid,mname,manufacture,expiry) values(%s,%s,%s,%s)",(null,mname,man,exp))
    mycon.commit() 
    cursor.close()
    mycon.close()
def new_pat_detail(pname,status,mid,dos,freq):
    cursor.execute("insert into patient(pid,pname,status,mid,dosage,frequency) values(%s,%s,%s,%s,%s,%s)",(null,pname,status,mid,dos,freq))
    mycon.commit()
    cursor.close()
    mycon.close()
def getmed():
    cursor.execute("select * from medicine;")
    med= cursor.fetchall()
    cursor.close()
    mycon.close()
    return med    
def getpat(pid):
    cursor.execute("select * from patient where pid =%s",(pid))
    pat= cursor.fetchone()
    cursor.close()
    mycon.close()
    return pat
def log(pid,mid,status):
    cursor.execute("insert into logs(srno,pid,mid,timestamp,status) values(%s,%s,%s,%s,%s)",(null,pid,mid,null,status)
    mycon.commmit()
    cursor.close()
    mycon.close()
"""
start=input("sign up/log in")
if start=="log in"
    print("enter the details below:\n")
    id = input("enter userid")
    
    
