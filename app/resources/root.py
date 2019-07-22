import os
import uuid
import json
import redis
from app.config import settings
from app.model import *

def set_cache(key, value):
	rclient = redis.Redis.from_url(settings.get('REDIS_URL'))
	rclient.set(key, json.dumps(value))

def get_cache(key):
	rclient = redis.Redis.from_url(settings.get('REDIS_URL'))
	return rclient.get(key)


class RootResources:
	def on_get(self, req, resp):
		if req.params.get('name'):
			self.sess.add(Countries(
				country_id= uuid.uuid4(),
				country_name= req.params.get('name')
			))
			self.sess.commit()
			
		countries_list = self.sess.query(Countries).all()
		resp.media = {
			"message": "Helloorld!",
			"country": [_country.repr for _country in countries_list]
		}


class RootNameResources:
	def on_post(self, req, resp, name):
		resp.media = {
			"message": "Hello, {}!".format(name.capitalize())
		}
