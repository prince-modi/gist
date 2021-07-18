from youtube_search import YoutubeSearch
from youtube_transcript_api import YouTubeTranscriptApi
import json
from youtube_search import YoutubeSearch

def sub_g(name):
    u = YoutubeSearch(name, max_results=1).to_json()
    x = json.loads(u)
    id = str()
    print(x['videos'])
    for item in x['videos']:
        id = item['link']
        id = id[9:]
    print(id)
    d = YouTubeTranscriptApi.get_transcript(id)
    S = list
    subs = "Start:"
    wc = 0
    for item in d:
        wc = wc + 1
        i = str(item['text'])
        #print(i)
        subs = subs + " " + i
    #print(subs)
    file = open("sfile.txt", "w+")
    file.write(subs)
    return id

#sub_g("the fermi paradox")
