from todo import db
from datetime import datetime
from flask_login import UserMixin
class User (db.Model ,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column (db.String(20), nullable = False)
    lname = db.Column (db.String(20), nullable = False)
    email = db.Column (db.String(50), nullable = False, unique = True)
    password = db.Column (db.String(50), nullable = False)
    is_active = True
    todos = db.relationship('Todo', backref = 'userid', lazy = True)
    def __repr__(self) :
        return f"{self.fname} {self.lname} ({self.email})"
class Todo(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    title = db.Column (db.String(30), nullable = False)
    content = db.Column (db.String(500), nullable = False)
    created_date = db.Column(db.DateTime, default = datetime.utcnow)
    due_date = db.Column(db.DateTime)
    author = db.Column (db.Integer, db.ForeignKey('user.id'), nullable = False)
    def __repr__(self):
        return f"{self.title} by {self.author.fname}"
