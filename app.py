from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' #Path to DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Just stops a warning.
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)

@app.route('/about')
def about():
    return "About"

if __name__ == "__main__":
    db.create_all() # Create Database
    app.run(debug=True)
