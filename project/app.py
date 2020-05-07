from flask import Flask, render_template, request
import psycopg2


def connect_db():
    global conn
    global cursor
    try:
        conn = psycopg2.connect(dbname='tftyiqbk', user='tftyiqbk', password='ioia30LFy_tPe-xsKDEfSalK-jlBC7j_'
                                , host='kandula.db.elephantsql.com')
        cursor = conn.cursor()
        cursor.execute('')
    except:
        print('please leave segevharpaz1.pythonanywhere.com and try again')


connect_db()
app = Flask(__name__)


@app.route('/')
def student():
   print(3)
   return render_template('projectHTML.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        result = str(result)[:-2]
        num = result.split(',')
        data = []
        for i in range(1, 6, 2):
            data.append(str(num[i][2:-2]))
        isit = False
        try:
            cursor.execute("SELECT * FROM project_the_one")
            table_data = cursor.fetchall()
            for row in table_data:
                for i in range(3):
                    if row[i] == data[i]:
                        isit = True
            if isit:
                try:
                    return render_template("projectHTML.html", result="change your name or password or phone_number")
                except:
                    print('please leave segevharpaz1.pythonanywhere.com and try again')
            else:
                sql = "INSERT INTO project_tho_one " \
                      "(name, password, phone_number, mac, connected_signup, connected_wifi) " \
                      "VALUES(%s, %s, %s, %s, %s, %s)"
                val = (data[0], data[1], data[2], 'miss_mac', True, False)
                try:
                    cursor.execute(sql, val)
                    vendor_id = cursor.fetchone()[0]
                    conn.commit()
                    return render_template('pass.html')
                except:
                    print('please leave segevharpaz1.pythonanywhere.com and try again')
        except:
            print('please leave segevharpaz1.pythonanywhere.com and try again')


@app.route('/sign_in')
def sign_in():
    return render_template('signin.html')


@app.route('/sign_in2', methods=['POST', 'GET'])
def sign_in2():
    if request.method == 'POST':
        result = request.form
        result = str(result)[:-2]
        num = result.split(',')
        data = []
        for i in range(1, 4, 2):
            data.append(num[i][2:-2])
            isit = False
        if isit:
            return render_template("sign_in.html", result="change your name or password")
        else:
            return render_template('pass.html')


if __name__ == '__main__':
   app.run(debug = True)
