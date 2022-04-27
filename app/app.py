from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('./index.html')

@app.route("/home")
def show_homepage():
    return render_template('./home.html')

@app.get("/about")
def show_about():
    return render_template('./about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')