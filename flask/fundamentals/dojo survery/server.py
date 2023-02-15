from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/show/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('result.html',name=session['name'],location=session['location'],language=session['language'],comment=session['comment'])
@app.route('/result')
def result():
    return render_template("result.html")



if __name__ == "__main__":
    app.run(debug=True)

