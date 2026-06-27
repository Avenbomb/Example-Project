import requests
from requests.exceptions import SSLError

BASE_URL = "https://httpbin.org"
TIMEOUT = 5


def print_response(label: str, resp: requests.Response) -> None:
    print(f"  {label}")
    print(f"  Status: {resp.status_code}")
    print(f"  URL:    {resp.url}")


def fetch(url: str, verify: bool | str) -> None:
    try:
        resp = requests.get(url, verify=verify, timeout=TIMEOUT)
        print_response("Success", resp)
    except SSLError as e:
        print(f"  SSLError: {e}")


def main():

    # --- Default: verify=True, requests uses its own CA bundle ---
    print("--- Valid cert, verification ON (default) ---")
    fetch(BASE_URL, verify=True)

    # --- Deliberately hit a bad cert site ---
    print("\n--- Bad cert, verification ON ---")
    fetch("https://expired.badssl.com/", verify=True)

    # --- Same bad cert, but skip verification ---
    print("\n--- Bad cert, verification OFF (insecure) ---")
    fetch("https://expired.badssl.com/", verify=False)

    # --- Point to a custom CA bundle (e.g. corporate/self-signed certs) ---
    # print("\n--- Custom CA bundle ---")
    # fetch(BASE_URL, verify="/path/to/custom-ca-bundle.crt")


if __name__ == "__main__":
    main()
