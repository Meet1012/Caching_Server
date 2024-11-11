from flask import Flask
from cachetools import cached, TTLCache
import requests
import argparse

app = Flask(__name__)

cache = TTLCache(maxsize=100, ttl=300)

@cached(cache,info=True)
def addCache(url):
    response = requests.request("GET", url)
    return response.content

@app.route("/<path:path>", defaults= {'path':''})
def check(path):
    response = addCache(path)
    print("Path", path)
    cache_hits = addCache.cache_info().hits
    if cache_hits == 0:
        print("X-Cache: MISS")
    else:
        print("X-Cache: HIT")
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int)
    args = parser.parse_args()
    app.run(port = args.port, debug = True)