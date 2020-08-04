from flask import Flask
from flask_restful import Api
from CarRestApi import CarsResource , AllFords , Test , GetPriceWise


app = Flask(__name__)
api = Api(app)

api.add_resource(CarsResource, '/Ford/<string:name>')
api.add_resource(AllFords, '/Ford')
api.add_resource(Test, '/SimilarName/<string:name>')
api.add_resource(GetPriceWise , '/BelowPrice/<string:price>')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NewData.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from db import db
db.init_app(app)
app.run(port=5000)
