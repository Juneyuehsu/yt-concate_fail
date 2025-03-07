<<<<<<< HEAD
import urllib.request
import json

from yt_concate.pipeline.steps.step import Step
from yt_concate.pipeline.steps.step import StepException
from yt_concate.settings import API_KEY
00

class GetVideoList(Step):
    def process(self, data, inputs):
=======
import urllib3.request
import jsons

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import API_KEY


class GetVideoList(Step):
    def process(self, inputs):
>>>>>>> origin/main
        channel_id = (inputs['channel_id'])
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
                                                                                                            channel_id)

        video_links = []
        url = first_url
        while True:
<<<<<<< HEAD
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)
=======
            inp = urllib3.request.urlopen(url)
            resp = jsons.load(inp)
>>>>>>> origin/main

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break

        print(video_links)
        return video_links
