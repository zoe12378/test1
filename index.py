from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>個人網頁</h1>"
    homepage += "<a href=/self>關於我</a><br>"
    return homepage

@app.route("/self")
def self():
    return render_template("self.html")


#if __name__ == "__main__":
#   app.run()