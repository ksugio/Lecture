import json
from urllib.request import urlopen
url = "https://raw.githubusercontent.com/ksugio/Lecture/master/DPNA/dummy/topRated.json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])
