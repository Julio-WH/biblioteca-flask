from flask_sqlalchemy import SQLAlchemy
from datetime import date
db = SQLAlchemy()


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    createdat = db.Column(db.Date, nullable=False, default=date.today)
    book = db.relationship('Books', backref='authors', lazy=True)

    def __repr__(self):
        return f'{self.name} {self.lastname}'


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    pub_date = db.Column(db.Date)
    createdat = db.Column(db.Date, nullable=False, default=date.today)
    autor_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    author = db.relationship('Authors', backref=db.backref('books', lazy=True))

    def __repr__(self):
        return f'{self.title}'