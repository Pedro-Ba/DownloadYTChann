import urllib.request
import json

def return_all_videos(yt_api_key, channel_id):
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + \
        'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(
        yt_api_key, channel_id)

    fileappend = open('all_links.txt', 'a')

    url = first_url
    while True:
        inp = urllib.request.urlopen(url, timeout=1)
        resp = json.load(inp)
        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                fileappend.write(base_video_url + i['id']['videoId'] + '\n')
        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
