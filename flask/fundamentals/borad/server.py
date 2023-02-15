from flask import Flask,render_template
app = Flask(__name__)    
@app.route('/')         
def test ():
    return render_template("index.html",row=8,col=8,color_one='red',color_two='black')
@app.route('/4')         
def lvltwo ():
    return render_template("index.html",row=8,col=4,color_one='red',color_two='black')
@app.route('/<int:x>/<int:y>')         
def lvlthree (x,y):
    return render_template("index.html",row=x,col=y,color_one='red',color_two='black')
@app.route('/<int:x>/<int:y>/<string:cone>/<string:ctwo>')         
def lvlfour (x,y,cone,ctwo):
    return render_template("index.html",row=x,col=y,color_one=cone,color_two=ctwo)
if __name__=="__main__":     
    app.run(debug=True)    

