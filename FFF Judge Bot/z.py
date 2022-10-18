import re
import pafy

msg = 'https://www.youtube.com/watch?v=yUwD8eOc97E'

#url = re.search(r'(\bhttps://www\.youtube\.com/watch.*)\b.*', msg)

#print(url.group(1))

#if re.search(r'\bhttps://www.youtube.com/watch\?', msg):
#	url = re.search(r'(\bhttps://www\.youtube\.com/watch.*)\b', msg).group(1)
#	video = pafy.new(url)
#	print(video.title)

url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
video = pafy.new(url)

print(video.title)