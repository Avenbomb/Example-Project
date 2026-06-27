import requests
from requests.exceptions import HTTPError

BASE_URL = "https://httpbin.org/basic-auth/user/pass"
TIMEOUT = 5  # seconds


def print_response(resp: requests.Response) -> None:
    print(f"  URL:      {resp.url}")
    print(f"  Status:   {resp.status_code} ({'OK' if resp.ok else 'FAIL'})")
    print(f"  Encoding: {resp.encoding}")
    print(f"  Elapsed:  {resp.elapsed.total_seconds():.3f}s")
    print(f"  Headers:  {dict(resp.headers)}")
    if resp.ok:
        print(f"  JSON:     {resp.json()}")


def fetch(session: requests.Session, auth: tuple) -> None:
    try:
        resp = session.get(BASE_URL, auth=auth, timeout=TIMEOUT)
        resp.raise_for_status()
        print_response(resp)
    except HTTPError as e:
        print(f"  HTTP error: {e}")
        print_response(e.response)


def main():
    with requests.Session() as session:
        print("--- Expected pass ---")
        fetch(session, auth=("user", "pass"))

        print("\n--- Expected fail ---")
        fetch(session, auth=("wrong", "pass"))


if __name__ == "__main__":
    main()
