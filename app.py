from flask_restful import Resource, Api
from flask import Flask, request
import requests
from . import create_app
from .views import PointView


app = create_app('default')
app_context = app.app_context()
app_context.push()
api = Api(app)

api.add_resource(PointView, '/song/<int:song_id>/rating')