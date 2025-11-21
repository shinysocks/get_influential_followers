#   Noah Dinan 2025
#   Get Influential Followers Script

#   This script will pull a list of the most
#   influential followers for any signed in instagram account!

# /// script
# requires-python = ">=3.14"
# dependencies = [ "instaloader", "browser_cookie3" ]
# ///

from os import system
from sys import exit, argv
from instaloader import LoginException, Instaloader, Profile

OUTPUT_FILE = "output.csv"

def is_follower_in_lines(follower: str, lines: list) -> bool:
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

    system(f"uv run instaloader --load-cookies={BROWSER}")

    try:
        f = open(OUTPUT_FILE, "x")
        f.close()
    except FileExistsError:
        print("found pre-existing output.txt file.")

    L = Instaloader(
        # user_agent = "", # might need this?
        download_pictures = False,
        download_videos = False,
        download_video_thumbnails = False,
        download_geotags = False,
        download_comments = False,
        max_connection_attempts = 5,
        request_timeout = 300.0,
        iphone_support = False
    )
    L.load_session_from_file(USER)
    profile = Profile.from_username(L.context, USER)
    print(f"found {profile.followers} followers for {USER}")

    print("loading followers into memory...", end='')

    followers = []
    for follower in profile.get_followers():
        followers.append(follower.username)

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
