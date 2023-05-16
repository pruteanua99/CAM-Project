import json
from urllib.request import urlopen


class location:
    def __init__(self):
        pass

    def getLocationDetails(self) -> str:
        url = "http://ipinfo.io/json"
        response = urlopen(url)
        data = json.load(response)

        return str(data)


if __name__ == "__main__":
    print(location.getLocationDetails())
