from flask_restful import Resource


class Home(Resource):
    def get(self):
        return {"message":"Hello from flask_restful!"}, 200