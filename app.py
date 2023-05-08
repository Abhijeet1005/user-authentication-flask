from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
dbs = SQLAlchemy(app)
app.app_context().push()


class credentials(dbs.Model):
    name = dbs.Column(dbs.Integer, primary_key=True)
    password = dbs.Column(dbs.String(30), nullable=False)


@app.route("/", methods=["GET", "POST"])
def homepage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
