import logging
import requests
import json
from datetime import datetime, timedelta

from timelyBot import TimelyBot

URL = "http://localhost:8000/api/getMeetings"


def makeAPIRequest() -> dict:
    data = requests.get(URL)
    return data.json()


def main():
    TimelyClient = TimelyBot()

    time = datetime.now() + timedelta(minutes=10)

    data = makeAPIRequest()
    print(json.dumps(data, indent=4))

    if (time.strftime("%M") == "00"):
        print("Someting")


if __name__ == "__main__":
    main()
