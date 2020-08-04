from flask_restful import Resource
from flask import Flask , request
from CarProfile import Car
class CarsResource(Resource):

    def get(self , name):
        car = Car.FindCar(name=name)

        if car:
            return car.json()
        return {'Message' : 'Car not found'}


    def post(self , name):
        data = request.get_json()

        item = Car(name , data['price'])
        item.AddNewCar()


    def put(self, name):
        data = request.get_json()
        item = Car.FindCar(name)

        if item:
            item.price = data['price']
        else:
            item = Car(name , data['price'])

        item.AddNewCar()

        return item.json()

class AllFords(Resource):

    def get(self):
        return {'Ford' : [car.json() for car in Car.query.all()]}


class Test(Resource):
    def get(self , name):

        return {'SimilarName' : [{n.name : n.price} for n in Car.query.filter_by(name=name).all()]}

class GetPriceWise(Resource):
    def get(self , price):
        items = []
        for n in Car.query.all():
            if n.price <= int(price) :
                items.append({n.name : n.price})



        return {'Price Below' : items}
