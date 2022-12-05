import json
from get_all_links import return_all_videos
from download_video_mp3 import download_video

configfile = open('config.json')

configjson = json.load(configfile)

configfile.close()

yt_api_key = configjson['key']
channel_id = configjson['channel_id']

#return_all_videos(yt_api_key, channel_id)

all_links = open('all_links.txt')

links = all_links.readlines()

download_video(links[0])

all_links.close()