from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "PPA Tool running on Azure (Flask Version)"

if __name__ == "__main__":
    app.run()
