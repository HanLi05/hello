from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    with open('welcome.html') as f:
        lines = f.read()
    return lines

@app.route('/login',methods = ['POST', 'GET'])
def login():
    with open('login.html') as f:
        lines = f.read()
    return lines
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug = True)

