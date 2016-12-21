from flask import Flask,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def accept_data():
    if request.method == "POST":
        data = request.get_data()
        import code
        code.interact(local=locals())
    return "done"

app.run(debug=True)
        
