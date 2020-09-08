from flask_restful import Resource, reqparse
from app.models.quotes import QuotesModel


class Quotes(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('quote',
                        type=str,
                        required=True,
                        help="This field cannot be blanks")

    parser.add_argument('author',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    def post(self):
        data = Quotes.parser.parse_args()
        query = QuotesModel.query.filter(QuotesModel.quote.ilike(f'%{data.quote}%')).first()
        if query:
            return {"message": "this quote already exists."}, 409
        else:
            row = QuotesModel()
            row.author = data.author.lower()
            row.quote = data.quote.lower()
            row.create()
            return {"message": "Quote added successfully."}, 201

class RandomQuote(Resource):
    def get(self):
        if QuotesModel.num_of_rows():
            data = QuotesModel.find_by_id(
                    randint(1, QuotesModel.num_of_rows())
                    )
            return {"author": data.author, "quote": data.quote}, 200
        return {"message": "uhh.. there is no quotes in database.!!"}, 404