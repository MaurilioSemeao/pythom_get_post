from flask import Flask, render_template, request
from calc_2grau import f_calc_2grau
from fahrenheit import cels_to_fahr

app = Flask(__name__)

@app.route('/')
def raiz():
    return render_template('index.html')

@app.route('/calculo2grau')
def calcula2grau():
    return render_template('calculo2grau.html')


@app.route('/fahrenheit')
def fahrenheit():
    return render_template('fahrenheit.html')


@app.route('/calc_2grau', methods=['POST'])
def calc_2grau():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    mss, x1, x2 = f_calc_2grau(a,b,c)
    res_equ = {"mss": mss, "x1": x1, "x2": x2 }

    return render_template('calculo2grau.html', res_equ = res_equ)


@app.route('/calc_fahrenheit')
def calc_fahrenheit():
    args = request.args
    celsius = float(args.get('celsius'))
    res_fahr = cels_to_fahr(celsius)

    return render_template('fahrenheit.html', res_fahr = f"{res_fahr:.2f}" )

if __name__ == '__main__':
    app.run(debug=True)