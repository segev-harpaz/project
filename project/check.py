from flask import Flask, render_template, request
import psycopg2


def connect_db():
    global conn
    global cursor
    global table_data
    try:
        conn = psycopg2.connect(dbname='tftyiqbk', user='tftyiqbk', password='ioia30LFy_tPe-xsKDEfSalK-jlBC7j_',
                                host='kandula.db.elephantsql.com')
    except:
        print('please leave segevharpaz1.pythonanywhere.com and try again')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM project_the_one")
    table_data = cursor.fetchall()


def do():
    global table_data
    global tablee
    global cursor
    tablee = []
    tablee.append(['name', 'password', 'connected'])
    for row in table_data:
        num = []
        if row[0] != 'admin':
            num.append(row[0])
            num.append(row[1])
            num.append(str(bool(row[4]) and bool(row[5])))
            tablee.append(num)
    return tablee


app = Flask(__name__)


@app.route('/')
def student():
    return render_template('projectHTML.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    global conn
    global cursor
    global table_data
    if request.method == 'POST':
        result = request.form
        result = str(result)[:-2]
        num = result.split(',')
        data = []
        for i in range(1, 6, 2):
            data.append(str(num[i][2:-2]))
        isit = False
        for row in table_data:
            for i in range(3):
                if data[i] == row[i]:
                    isit = True
        if isit:
            try:
                return render_template("projectHTML.html", result="change your name or password or phone_number")
            except:
                print('please leave segevharpaz1.pythonanywhere.com and try again')
        else:
            print(data[0])
            print(data[1])
            print(data[2])
            sql = "INSERT INTO project_the_one (name, password, phone_number, mac, connected_signup, connected_wifi) " \
                  "VALUES(%s, %s, %s, %s, %s, %s)"
            val = (data[0], data[1], data[2], 'miss_mac', True, False)
            cursor.execute(sql, val)
            conn.commit()
            return render_template('pass.html')


@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        return render_template('signin.html')


@app.route('/sign_in2', methods=['POST', 'GET'])
def sign_in2():
    global table_data
    global tablee
    if request.method == 'POST':
        result = request.form
        result = str(result)[:-2]
        num = result.split(',')
        data = []
        for i in range(1, 4, 2):
            data.append(num[i][2:-2])
        isit = False
        for i in table_data:
            if i[0] == data[0] and i[1] == data[1]:
                isit = True
        if data[0] == 'admin' and data[1] == 'admin123':
            do()
            return render_template('admin.html', tablee=tablee)
        elif isit:
            return render_template('pass.html')
        else:
            return render_template("signin.html", result="change your name or password")


@app.route('/delete', methods = ['POST', 'GET'])
def delete():
    global table_data
    global cursor
    global data
    global conn
    if request.method == 'POST':
        result = request.form
        result = str(result)[:-2]
        result = result.split(',')
        result = result[1][2:-2]
        checker = False
        for row in table_data:
            if row[0] == result:
                checker = True
        if checker:
            delete_sql = 'DELETE FROM project_the_one WHERE name = %s'
            cursor.execute((delete_sql), (result,))
            conn.commit()
            cursor.close()
            conn.close()
            connect_db()
            do()
            return render_template('admin.html', tablee=tablee)
        else:
            return render_template('admin.html', pro='this user is not exist in the database', tablee=tablee)


if __name__ == '__main__':
    connect_db()
    app.run(debug = True)
