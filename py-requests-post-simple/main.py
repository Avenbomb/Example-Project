import requests


def main():
    title = "Hellow Interweb"
    body = "My first post"
    user_id = 255
    payload = {"title": title, "body": body, "userID": user_id}

    post_url = "https://jsonplaceholder.typicode.com/posts"

    resp = requests.post(post_url, json=payload)
    resp.raise_for_status()
    print(resp.json()["id"])


if __name__ == "__main__":
    main()
