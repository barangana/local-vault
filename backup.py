import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

def load_configs():
    with open("configs.json", "r") as file:
        data = json.load(file)
        return data

def save_configs(configs):
    with open("configs.json", "w") as file:
        json.dump(configs, file, indent=2)

def download_backup(repo_name, username, headers, backup_dir, timestamp):
    response = requests.get(f"https://api.github.com/repos/{username}/{repo_name}/zipball", headers=headers)

    if response.status_code == 200:
        filename = f"{repo_name}_{timestamp}.zip"
        filepath = os.path.join(backup_dir, filename)
        with open(filepath, "wb") as file:
            file.write(response.content)
            print(f"Downloaded {repo_name} to {filepath}")
    else:
        print(f"Failed to download {repo_name} to {filepath}. Status code: {response.status_code}")

def main():
    load_dotenv()
    configs = load_configs()

    backup_dir = configs["backup_dir"]
    username = configs["username"]
    repos_to_track = configs["repos_to_track"]
    bearer_token = os.getenv("BEARER_TOKEN")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get("https://api.github.com/user/repos", headers=headers)
    data = response.json()

    for tracked_repo in repos_to_track:
        for repo in data:
            if tracked_repo["name"] == repo["name"]:
                config_pushed_at = tracked_repo["pushed_at"]
                github_pushed_at = repo["pushed_at"]

                if config_pushed_at != github_pushed_at:
                    download_backup(repo["name"], username, headers, backup_dir, timestamp)
                    tracked_repo["pushed_at"] = repo["pushed_at"]
                    tracked_repo["last_back_up"] = timestamp
                else:
                    print(f"{repo['name']} is up to date. Skipping.")

    save_configs(configs)

if __name__ == "__main__":
    main()
