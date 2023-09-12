from . import db

class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    createdat = db.Column(db.Date, nullable=False, default=date.today)
    book = db.relationship('Books', backref='Authors', lazy=True)

    def __repr__(self):
        return f'{self.name} {self.lastname}'


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    pub_date = db.Column(db.Date)
    createdat = db.Column(db.Date, nullable=False, default=date.today)
    autor_id = db.Column(db.Integer, db.ForeignKey('Authors.id'), nullable=False)

    def __repr__(self):
        return f'{self.title}'