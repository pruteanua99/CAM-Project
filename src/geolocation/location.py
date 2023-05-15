import json
from urllib.request import urlopen


def getLocationDetails() -> str:
    url = "http://ipinfo.io/json"
    response = urlopen(url)
    data = json.load(response)

    return str(data)


if __name__ == "__main__":
    print(getLocationDetails())
