from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'  
@app.route('/dojo')          
def dojo():
    return 'Dojo'
@app.route('/say/<call>')          
def say(call):
    return 'Hi '+ call
@app.route('/repeat/<string:id>/<int:num>')          
def times(id,num):
    return id * num
if __name__=="__main__":     
    app.run(debug=True)   




