from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def main():
    myObj = {"name":"John", "age":30, "car":"mercadies"}
    return myObj

@app.route('/ajaxgrab',methods = ['POST','GET'])
def ajaxgrab():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)