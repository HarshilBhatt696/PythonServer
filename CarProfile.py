
from db import db


class Car(db.Model):
    __tablename__ = 'ford'

    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))


    def __init__(self , name , price):
        self.name = name
        self.price = price

    def json(self):
        return {'name' : self.name , 'price' : self.price}

    @classmethod
    def FindCar(self , name):
        return self.query.filter_by(name=name).first()


    def SimilarName(self , name):
        item = {name : [n for n in self.query.filter_by(name=name).all()]}
        return item


    def AddNewCar(self):
        CheckCar = self.FindCar(self.name)
        if CheckCar is None:
            db.session.add(self)
            db.session.commit()
