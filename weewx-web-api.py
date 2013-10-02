from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

from database import Database

app = Flask(__name__)
api = Api(app)


class LatestWeather(Resource):
    
    def __init__(self):
        self.db = Database()

    def get(self):
        weather = self.db.get_latest_weather()
        return weather


class Weather(Resource):
    
    def __init__(self):
        self.db = DatabaseConnection()

    def get(self, weather_id):
        weather = self.db.get_weather_by_id(weather_id)
        return weather

api.add_resource(LatestWeather, '/weather/latest')
api.add_resource(Weather, '/weather/<string:id>')


if __name__ == '__main__':
    app.run(debug=True)

