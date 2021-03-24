import requests

r=requests.get("http://www.kennesaw.edu")

print(r)
print(r.status_code)
#print(r.status)
print(r.headers)
print(r.headers['date'])
#print(r.text)