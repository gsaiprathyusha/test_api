from flask import Flask
import pymysql

app=Flask(__name__)

@app.route('/')
def home():
    connection=pymysql.connect(host='localhost',
                               user='root',
                               password='Sai@221100',
                               db='testapi',
                               cursorclass=pymysql.cursors.DictCursor)
    mycursor=connection.cursor()
    mycursor.execute('select * from testapi.emp')
    return str(mycursor.fetchall())
    #return "Hello World!!"

app.run(port="5000",debug=True)