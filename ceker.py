import requests

with open("urls.txt", "r") as f:
    urls = f.readlines()

for url in urls:
    response = requests.get(url.strip())
    if response.status_code == 401:
        print("Forbidden")
    elif response.status_code == 200:
        print("OK")
