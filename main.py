import urllib
import json

configfile = open('config.json')

configjson = json.load(configfile)

configfile.close()

yt_api_key = configjson['key']
channel_id = configjson['channel_id']