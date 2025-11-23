#   Noah Dinan 2025
#   Get Influential Followers Script

#   This script will pull a list of the most
#   influential followers for any signed in instagram account!

# /// script
# requires-python = ">=3.12"
# dependencies = [ "instaloader", "browser_cookie3" ]
# ///

from os import system
from pathlib import Path
from sys import exit, argv
from instaloader import Instaloader, Profile, ConnectionException

OUTPUT_FILE = "output.csv"
FOLLOWERS_FILE = "followers.txt"


def is_follower_in_lines(follower: str, lines: list[str]) -> bool:
    for line in lines:
        if follower in line:
            return True
    return False


def main():
    if len(argv) < 3:
        print("could not find <username> or <browser> in arguments")
        exit(1)

    USER = argv[1]
    BROWSER = argv[2]

    try:
        f = open(OUTPUT_FILE, "x")
        f.close()
    except FileExistsError:
        print("found pre-existing output.txt file.")

    L = Instaloader(
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        max_connection_attempts=10,
        request_timeout=300.0,
        iphone_support=False
    )

    follower_count = 0
    followers: list[str] = []

    if (Path(FOLLOWERS_FILE).exists()):
        print(f"followers already loaded into {FOLLOWERS_FILE}")
        with open(FOLLOWERS_FILE, "r+") as ff:
            followers = ff.read().splitlines()
    else:
        system(f"uv run instaloader --load-cookies={BROWSER}")
        L.load_session_from_file(USER)
        profile = Profile.from_username(L.context, USER)
        print(f"found {profile.followers} followers for {USER}")

        print("loading followers into memory...", flush=True)

        for follower in profile.get_followers():
            followers.append(follower.username)
            follower_count += 1
            if follower_count % 50 == 0:
                print(f"{follower_count}/{profile.followers}")

        with open(FOLLOWERS_FILE, "w+") as ff:
            for follower in followers:
                ff.write(follower + "\n")

    print("done")

    current_lines = []
    with open(OUTPUT_FILE, "r+") as file:
        current_lines = file.readlines()

    f = open(OUTPUT_FILE, "a")

    print(f"updating followers in {OUTPUT_FILE}")

    for follower in followers:
        if not is_follower_in_lines(follower, current_lines):
            try:
                n = Profile.from_username(L.context, follower).followers
                f.write(f"{follower}, {n}\n")
            except KeyboardInterrupt:
                f.close()
                exit()
            except ConnectionException:
                print("rate-limit hit, please wait a few minutes and rerun script")
                f.close()
                exit()
            print(f"added {follower}")
        else:
            print(f"already added {follower}")

    f.close()

    with open(OUTPUT_FILE, "r+") as file:
        lines = file.readlines()
        lines.sort(reverse=True, key=lambda x: int(x.split(",")[1].strip()))
        file.seek(0)
        file.truncate()
        file.writelines(lines)


if __name__ == "__main__":
    main()
