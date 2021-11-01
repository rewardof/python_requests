import requests

data = requests.get('https://www.youtube.com/watch?v=s7M9Spy7P-c&ab_channel=NilufarbintuUlug%27bek')
print(data.headers)
print(data.json)
print(dir(data))
print(data.history)
print(data.text)
print(data.content)
print(data.url)
with open('rtr.mp4', 'wb') as f:
    f.write(data.content)