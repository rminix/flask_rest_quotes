from app import db
from sqlalchemy import orm, func

class QuotesModel(db.Model):
    __tablename__ = 'quotes'
    _id = db.Column(db.Integer, primary_key=True)
    quote =  db.Column(db.string(255), nullable=False )
    author = db.Column(db.string(60), nullable=False) 

    normalize_quote = orm.column_property(func.lower(quote))
    normalize_author = orm.column_property(func.lower(author))



    def create(self):
        db.session.add(self)
        db.session.commit()