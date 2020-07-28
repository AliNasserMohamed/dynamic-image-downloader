import requests
import json
with open("souq.json", "r") as j:
    f = json.load(j)
    for i in f:
        r = requests.get(i["img"])
        with open("images\\"+i["name"]+".jpg", "wb") as f:
            f.write(r.content)
