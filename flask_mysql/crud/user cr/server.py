from flask import Flask , render_template
from useres import User
app = Flask(__name__)    
@app.route('/')          
def create():
    return render_template('index.html')

if __name__=="__main__":  
    app.run(debug=True)    
