from flask import Flask
from api.api import Api

app = Flask(__name__)

api = Api(app)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')


    