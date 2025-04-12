import requests

def fetch_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/100"

    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        jokes_list = data["data"]
        joke = jokes_list["categories"]
        return joke
    else:
        raise Exception("Failed to load jokes")

def main():
    try:
        jokes = fetch_jokes()
        print(jokes)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
