from app import db
from sqlalchemy import orm, func

class QuotesModel(db.Model):
    __tablename__ = 'quotes'
    _id = db.Column(db.Integer, primary_key=True)
    quote =  db.Column(db.String(255), nullable=False )
    author = db.Column(db.String(60), nullable=False) 

    normalize_quote = orm.column_property(func.lower(quote))
    normalize_author = orm.column_property(func.lower(author))



    def create(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def num_of_rows():
        return db.session.query(QuotesModel).count()

    @classmethod
    def find_by_id(cls, num):
        return db.session.query(QuotesModel).get_or_404(num)

    