from flask import Flask

app = Flask(__name__) #app is the name of the object here

@app.route('/')
def home():
  return "<h1> Hello World </h1>"

@app.route('/hello')
def hello():
  return "<h3> This is hello 2 </h3>"

if __name__ =="__main__":
  app.run(debug=True,port=8080)