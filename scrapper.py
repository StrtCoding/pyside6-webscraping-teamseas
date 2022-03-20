import requests


URL = "https://tscache.com/donation_total.json"


def get_pounds_count():
    response = requests.get(URL)
    pounds_count = response.json()

    return pounds_count["count"]


if __name__ == "__main__":
    print(get_pounds_count())



