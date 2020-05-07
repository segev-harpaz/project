
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


@app.route('/sign_in',methods = ['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        return render_template('signin.html')


@app.route('/sign_in2',methods = ['POST', 'GET'])
def sign_in2():
    global table_data
    if request.method == 'POST':
        result = request.form
        result = str(result)[:-2]
        num = result.split(',')
        data = []
        for i in range(1, 4, 2):
            data.append(num[i][2:-2])
        isit = False
        for i in table_data:
            if  i[0] == data[0] and i[1] == data[1]:
                isit = True
        if data[0] == 'admin' and data[1] == 'admin123':
            isit = False
            do()
            return render_template('admin.html', tablee=tablee)


            @app.route('/sign_in2/delete',methods = ['POST', 'GET'])
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


        if isit:
            return render_template("sign_in.html", result="change your name or password")
        else:
            return render_template('pass.html')