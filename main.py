import logging
from flask import Flask
from flask import url_for, request, render_template
from flask_restful import Resource, Api

# EDA Packages
# import pandas as pd
# import numpy as np

# ML Packages
app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return {'about' : 'Hello Flask!'}


    def post(self):
        some_json = request.get_json()
        return {'you sent' : some_json}, 201


class Multi(Resource):
    def get(self, num):
        return {'result' : num*10}

api.add_resource(Hello, '/')
api.add_resource(Multi, '/multi/<int:num>')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
    # app.run(host="127.0.0.1", port=8080, debug=True)
