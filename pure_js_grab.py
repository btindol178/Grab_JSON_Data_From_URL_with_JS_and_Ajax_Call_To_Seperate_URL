from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def main():
    myObj = {"name":"John", "age":30, "car":"mercadies"}
    return myObj

@app.route('/jsgrab',methods = ['POST','GET'])
def ajaxgrab():
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug=True)