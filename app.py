from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      num =str(result).split(',')
      x = num[1][2:-2]
      print(x)
      return render_template("pass.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)