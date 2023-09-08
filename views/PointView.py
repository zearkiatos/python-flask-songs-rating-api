from flask_restful import Resource
from flask import request
import requests
from http import HTTPStatus
from ..config import Config
import json
from celery import Celery

config = Config()

celery_app = Celery('tasks', broker=f'{config.REDIS_BROKER_BASE_URL}/0')

@celery_app.task(name='table.registry')
def point_registry(song_json):
    pass

class PointView(Resource):
    def post(self, song_id):
        data = {
            'username': config.SONGS_API_USERNAME,
            'password': config.SONGS_API_PASSWORD
        }
        response = requests.post(f'{config.SONGS_API_BASE_URL}/login',json=data)
        if response.status_code == HTTPStatus.OK:
            data = response.json()
            accessToken = data['accessToken']

            headers = {
                'Authorization': f'Bearer {accessToken}'
            }
            content = requests.get(f'{config.SONGS_API_BASE_URL}/song/{song_id}', headers=headers)

            if content.status_code == HTTPStatus.NOT_FOUND:
                return content.json(), HTTPStatus.NOT_FOUND
            else:
                song = content.json()
                song['point'] = request.json['point']
                args = (song,)
                point_registry.apply_async(args)
                return json.dumps(song)
        else:
            return {
                'message': 'Access denied'
            }, HTTPStatus.FORBIDDEN
