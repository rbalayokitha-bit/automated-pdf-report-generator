import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_posts(limit=10):

    try:
        response = requests.get(
            API_URL,
            params={"_limit": limit},
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data

    except requests.exceptions.RequestException as error:

        raise RuntimeError(f"API Error: {error}")


if __name__ == "__main__":

    posts = fetch_posts(5)

    print("API Connection Successful!")
    print("Total Posts:", len(posts))

    for post in posts:

        print("----------------------")
        print("ID:", post["id"])
        print("Title:", post["title"])