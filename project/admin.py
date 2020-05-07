from flask import Flask, render_template, request
import psycopg2


def connect_db():
    global table_data
    global cursor
    global conn
    conn = psycopg2.connect(dbname='tftyiqbk', user='tftyiqbk', password='ioia30LFy_tPe-xsKDEfSalK-jlBC7j_'
                            , host='kandula.db.elephantsql.com')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM project_the_one")
    table_data = cursor.fetchall()


app = Flask(__name__)


def do():
    global table_data
    global data
    global cursor
    data = []
    data.append(['name', 'password', 'connected'])
    for row in table_data:
        num = []
        if row[0] != 'admin':
            num.append(row[0])
            num.append(row[1])
            num.append(str(bool(row[4]) and bool(row[5])))
            data.append(num)
    return data


@app.route('/')
def dodo():
    global data
    return render_template('admin.html', data=data)


@app.route('/delete',methods = ['POST', 'GET'])
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
        print(checker)
        if checker:
            delete_sql = 'DELETE FROM project_the_one WHERE name = %s'
            cursor.execute((delete_sql), (result,))
            conn.commit()
            cursor.close()
            conn.close()
            connect_db()
            data = do()
            print(data)
            return render_template('admin.html', data=data)
        else:
            return render_template('admin.html', pro='this user is not exist in the database', data=data)


if __name__ == '__main__':
    connect_db()
    do()
    app.run()
