from flask import Flask
from flask_restful import Api ,Resource

from resources.sensor import SensorRegister, Sensors 

app = Flask(__name__)
app.secret_key = 'dature'  
api = Api(app)

class Home(Resource):
    def get(self):
        return "This is test API, Welcome :)"
 
# http://127.0.0.1:5000 
api.add_resource(Home, '/') 
# Mongodb List all collection values /get
api.add_resource(SensorRegister, "/sensors")                      
# For collect wemos data from specific id /post
# return specific id's sensor datas /get
api.add_resource(Sensors, "/sensor/<string:sensor_id>")

# If the debug flag is 'True' set the server 
# will automatically reload for code changes 
# and show a debugger in case an exception happened.
if __name__ == "__main__":
    from database import db
    db.initialize()
    app.run(port=5000, debug=True, threaded = True)
    






