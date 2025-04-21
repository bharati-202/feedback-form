from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedbacks.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Feedback {self.name}>'
    
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    feedback = request.form["feedback"]
    
    if not name or not email or not feedback:
        return render_template("index.html", error="All fields are required!")
    
    fb = Feedback(name=name, email=email, feedback=feedback)
    
    db.session.add(fb)
    db.session.commit()
    
    return render_template("thankyou.html", name=name)

@app.route("/feedbacks")
def all_feedbacks():
    feedbacks = Feedback.query.all()
    return {"feedbacks": [{"name": fb.name, "email": fb.email, "feedback": fb.feedback} for fb in feedbacks]}
    
@app.route("/all-feedbacks")
def show_feedback():
    feedbacks = Feedback.query.all()
    return render_template("all_feedbacks.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)
