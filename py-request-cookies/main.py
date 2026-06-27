import requests

BASE_URL = "https://httpbin.org"
TIMEOUT = 5


def print_cookies(label: str, jar: requests.cookies.RequestsCookieJar) -> None:
    print(f" {label}: {dict(jar)}")


def main():
    with requests.Session() as session:
        # Set a cookie via the server
        resp = session.get(
            f"{BASE_URL}/cookies/set", params={"flavour": "strawberry"}, timeout=TIMEOUT
        )
        print_cookies("Session cookies after set", session.cookies)

        # Get cookies from the session
        resp = session.get(f"{BASE_URL}/cookies", timeout=TIMEOUT)
        print(f"JSON: {resp.json()}")

        # POST with a manually added cookie
        resp = session.post(
            f"{BASE_URL}/post", cookies={"toppings": "sprinkles"}, timeout=TIMEOUT
        )
        print(f"  Cookies seen by server: {resp.json()['headers'].get('Cookie')}")


if __name__ == "__main__":
    main()
