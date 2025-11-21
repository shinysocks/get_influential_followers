## Dependencies
* [uv](https://docs.astral.sh/uv/getting-started/installation/)
* Some modern browser [brave, chrome, edge, firefox, safari] signed into the instagram account you want to use
* Instagram username

## How to use this script
```bash
uv run get_influential_followers.py USERNAME BROWSER
```

### for example using francesca hong's account with a session in the chrome browser:
```bash
uv run get_influential_followers.py francescahongwi chrome
```

> [!NOTE]
> This script is resumable and will pick up where it left off if it is cancelled
