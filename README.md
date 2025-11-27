## Dependencies
* [uv](https://docs.astral.sh/uv/getting-started/installation/)
* [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* Some modern browser [brave, chrome, edge, firefox, safari] signed into the instagram account you want to use
* Instagram username

## How to use `get_influential_followers.py`
```bash
uv run get_influential_followers.py USERNAME BROWSER
```

### for example using francesca hong's account with a session in the chrome browser:
```bash
uv run get_influential_followers.py francescahongwi chrome
```
> [!NOTE]
> This script is resumable and will pick up where it left off if it is cancelled. After retrieving the initial followers list,
> the script retrieves follower counts for each username without signing in to the original account.

## How to use `cycle_ec2_ip.sh`
```bash
aws login
. cycle_ec2_ip.sh
```
> [!NOTE]
> Use crontab to automatically start the python script when the ec2 instance is started and initial followers.txt
> data has already been retrieved.
> ```
> # crontab
> @reboot (cd /home/ec2-user && uv run get_influential_followers.py a b)
> ```

