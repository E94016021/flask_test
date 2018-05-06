import requests

r = requests.get('http://www.google.com')
# requests.post()

print(r.content)
