from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/ex0')
def f_ex0():
    return '<html> <body><h1>Hola, Flask!</h1> </body> </html> '



@app.route('/ex1')
def f_ex1():
    return render_template('/ex1.html')

@app.route('/ex2')
def f_ex2():
    return render_template('ex2.html', modul='M02', nota=8)



@app.route('/ex3/<modul>/<int:nota>')
def f_ex3(modul, nota):
    return render_template('ex2.html', modul=modul , nota=nota) 

@app.route('/ex4')
def ex4():
    var1 = request.args.get('var1', default = 'No modul' , type=str)
    var2 = request.args.get('var2', default = 33 , type=int)
    return render_template('ex2.html', modul=var1, nota=var2)
