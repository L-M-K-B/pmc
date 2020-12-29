from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://laura@localhost:5432/db_web_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Heights(db.Model):
    __tablename__ = "heights"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    height = db.Column(db.Integer, nullable=False)

    def __init__(self, email_, height_):
        self.email = email_
        self.height = height_


# db.create_all()


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/success/", methods=['POST'])
def success_page():
    if request.method == 'POST':
        try:
            email = request.form["email_name"]
            height = request.form["height_name"]
            entry = Heights(email, height)
            db.session.add(entry)
            db.session.commit()
        except:
            db.session.rollback()
            print(sys.exc_info())
        finally:
            db.session.close()

    return render_template("success.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
