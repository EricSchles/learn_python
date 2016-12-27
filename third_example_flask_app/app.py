from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/<name>",methods=["GET","POST"])
def index(name="nothing"):
    if name!="nothing":
        return "hello "+name
    else:
        return "hello Shalmali"

app.run(debug=True)
