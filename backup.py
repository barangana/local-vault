#curl -L \
#  -H "Accept: application/vnd.github+json" \
#  -H "Authorization: Bearer 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" \
#  -H "X-GitHub-Api-Version: 2026-03-10" \
#  https://api.github.com/repos/barangana/pantry


import requests
import json
import os
from dotenv import load_dotenv

def load_configs():
    with open("configs.json", "r") as file:
        data = json.load(file)
        return data


def main():
    load_dotenv()
    configs = load_configs()

    username = configs["username"]
    repos_to_track = configs["repos_to_track"]
    bearer_token = os.getenv("BEARER_TOKEN")

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get("https://api.github.com/user/repos", headers=headers)
    data = response.json()

    # print(json.dumps(data, indent=2))

    for repo in data:
        if repo["name"] in repos_to_track:
            print(repo["name"])
            print(repo["pushed_at"])
            print(True)

if __name__ == "__main__":
    main()
