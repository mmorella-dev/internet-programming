from flask import Flask, request
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from sqlalchemy import create_engine, text
from json import dumps

SQLITE_FILE = "measures.db"
SERVER_PORT = 9000

db_connect = create_engine(f'sqlite:///{SQLITE_FILE}')
app = Flask(__name__)
api = Api(app)

class Areas(Resource):
  def get(self):
    with db_connect.connect() as conn:
        result = conn.execute(text("select area_id, name, latitude as lat, longitude as long from area")) # This line performs query and returns json result
        return [dict(zip(tuple(row._fields), row)) for row in result.all()]


class AreaLocations(Resource):
  def get(self, area_id):
    with db_connect.connect() as conn:
        # This line performs query and returns json result
        result = conn.execute(
            text("select location_id as loc_id, name, altitude as alt, location_area as area_id from location where location_area = %d" %int(area_id)))
        return [dict(zip(tuple(row._fields), row)) for row in result.all()]


class LocationMeasurements(Resource):
  def get(self, loc_id):
    with db_connect.connect() as conn:
        # This line performs query and returns json result
        result = conn.execute(
            text("select measurement_id as m_id, measurement_location as loc_id, value as val from measurement where measurement_location = %d" % int(loc_id)))
        return [dict(zip(tuple(row._fields), row)) for row in result.all()]


class AreaCategories(Resource):
  def get(self, area_id):
    with db_connect.connect() as conn:
        # This line performs query and returns json result
        result = conn.execute(
            text("SELECT category_id AS cat_id, name, description FROM category WHERE category_id IN (SELECT category_id FROM category_area WHERE area_id = %d)" % int(area_id)))
        return [dict(zip(tuple(row._fields), row)) for row in result.all()]


class AreaAverageMeasurement(Resource):
  def get(self, area_id):
    with db_connect.connect() as conn:
        # This line performs query and returns json result
        result = conn.execute(
            text("SELECT AVG(value) AS avg FROM measurement WHERE measurement_location IN (SELECT location_id FROM location WHERE location_area = %d)" % int(area_id)))
        return result.all()[0]["avg"]


class AreaNumberLocations(Resource):
  def get(self, area_id):
    with db_connect.connect() as conn:
        # This line performs query and returns json result
        result = conn.execute(
            text("SELECT COUNT(*) AS count FROM location WHERE location_area = %d" % int(area_id)))
        return result.all()[0]["count"]


api.add_resource(Areas, '/area')
api.add_resource(AreaLocations, '/area/<area_id>/location')
api.add_resource(LocationMeasurements, '/location/<loc_id>/measurement')
api.add_resource(AreaCategories, '/area/<area_id>/category')
api.add_resource(AreaAverageMeasurement, '/area/<area_id>/average_measurement')
api.add_resource(AreaNumberLocations, '/area/<area_id>/number_locations')


if __name__ == '__main__':
    app.run(port=SERVER_PORT)
