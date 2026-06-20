from pprint import pprint

import requests


def main():
    player = "Salvsis2"
    hiscores_base_url = (
        "http://secure.runescape.com/m=hiscore_oldschool/index_lite.json?player="
    )
    resp = requests.get(hiscores_base_url + player)
    print(resp)
    pprint(resp.json())


if __name__ == "__main__":
    main()
