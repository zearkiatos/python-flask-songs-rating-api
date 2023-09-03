from flask_restful import Resource
from flask import request
import requests
from http import HTTPStatus
from ..config import Config
import json

config = Config()

class PointView(Resource):
    def post(self, song_id):
        data = {
            'username': config.SONGS_API_USERNAME,
            'password': config.SONGS_API_PASSWORD
        }
        response = requests.post(f'{config.SONGS_API_BASE_URL}/login',json=data)
        if response.status_code == HTTPStatus.OK:
            print(response.content)
            data = response.json()
            accessToken = data['accessToken']

            print(accessToken)

            headers = {
                'Authorization': f'Bearer {accessToken}'
            }
            content = requests.get(f'{config.SONGS_API_BASE_URL}/song/{song_id}', headers=headers)

            if content.status_code == HTTPStatus.NOT_FOUND:
                return content.json(), HTTPStatus.NOT_FOUND
            else:
                song = content.json()
                print(song)
                song['point'] = request.json['point']
                args = (song,)
                return json.dumps(song)
        else:
            return {
                'message': 'Access denied'
            }, HTTPStatus.FORBIDDEN
