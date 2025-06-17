from flask import Flask, render_template, request

app = Flask(__name__)


mysql = MySQL(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

    return "Data inserted successfully !"

if __name__ == "__main__":
    app.run(debug=True)
