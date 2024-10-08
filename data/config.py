# api id, hash
API_ID = 26715592
API_HASH = '87f66d4ba46c5d15eda3965ac41c4c33'

REF_LINK = "t.me/vertus_app_bot/app?startapp=303199608"

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'REPEAT': [300, 600],
    'BUY_CARD': [2, 5]   # delay before buy a upgrade cards
}

# need buy a cards
BUY_CARD = True

# need buy upgrades
BUY_UPGRADE = True

PROXY = {
    "USE_PROXY_FROM_FILE": True,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "socks5",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "socks5"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}
# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30
