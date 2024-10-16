#!/usr/bin/env python3
import requests
import datetime

jobs = requests.get("https://jobb.forsvarsmakten.se/api/jobs").json()

s = 0
for job in jobs["jobs"]:
    start = job["pubDate"]
    end = job["pubDateTo"]

    days = (
        datetime.datetime.strptime(end, "%Y-%m-%d")
        - datetime.datetime.strptime(start, "%Y-%m-%d")
    ).days

    if days >= 90:
        s += days * int(job["id"])


print("MyrCTF{" + f"{s}" + "}")
