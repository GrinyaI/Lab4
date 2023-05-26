from flask import Flask, render_template, request, url_for
from Funct import writetofile, check, checkau

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/authorization', methods=['post', 'get'])
def authoriz():
    data = {}
    au = ''
    with open('Bd.txt', 'r') as file:
        for line in file:
            key, *value = line.split()
            data[key] = value
    if request.method == 'POST':
        log = str(request.form.get('login').strip())
        pas = str(request.form.get('password').strip())
        au = checkau(data, log, pas)
    return render_template('authorization.html', ath=au)

@app.route('/registration', methods=['post', 'get'])
def registr():
    data = {}
    reg = ''
    if request.method == 'POST':
        log = str(request.form.get('login').strip())
        pas = str(request.form.get('password').strip())
        with open('Bd.txt', 'r') as file:
            for line in file:
                key, *value = line.split()
                data[key] = value
            if check(data, log):
                reg = 'Данный логин занят'
            else:
                reg = writetofile(log, pas)
    return render_template('registration.html', regis=reg)
