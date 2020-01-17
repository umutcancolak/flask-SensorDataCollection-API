from database import db
import datetime

class SensorModel(object):
    def __init__(self, _id, moisture, temperature, date=datetime.datetime.now()):
        self._id = _id
        self.date = date
        self.moisture = moisture
        self.temperature = temperature       
    
    @staticmethod
    def get_all():
        return [result for result in db.find("sensor_data",{})]

    @staticmethod
    def find_by_id(sensor_id):
        return [data for data in db.find("sensor_data",{"id":sensor_id})]

    def save_to_mongo(self):
        db.insert("sensor_data",self.json())

    def json(self):
        """
        To return Json for database
        """
        return {
            "id": self._id,
            "date": self.date,
            "temperature": self.temperature,
            "moisture" : self.moisture
        }

    def jsonify(self):
        """
        To return Json as string
        """
        return {
            "id": self._id,
            "date": self.date.strftime("%m/%d/%Y, %H:%M:%S"),
            "temperature": self.temperature,
            "moisture" : self.moisture
        }
