# Local Vault

A Python script that automatically backs up your GitHub repositories as timestamped ZIP files to your local machine. Only downloads repositories that have been updated since the last backup.

## Prerequisites
 
- Python 3.x
- pip3

## Installation
 
1. Clone or download this repository to your local machine.
2. Install the required dependencies:
```bash
pip3 install requests python-dotenv
```

## Configuration
 
### 1. Set up your environment variables
 
Rename `.env.local` to `.env`:
 
```bash
mv .env.local .env
```
 
Open `.env` and replace the placeholder with your GitHub Bearer token:
 
```
BEARER_TOKEN=your_github_token_here
```
 
### 2. Set up your config file
 
Rename `template.json` to `configs.json`:
 
```bash
mv template.json configs.json
```
 
Open `configs.json` and fill in your own values:
 
```json
{
  "username": "your_github_username",
  "repos_to_track": [
    {
      "name": "your-repo-name",
      "pushed_at": "",
      "last_back_up": ""
    }
  ],
  "backup_dir": "/your/local/backup/path"
}
```
 
- `username` — your GitHub username
- `backup_dir` — the full path to the folder where ZIP files will be saved
- `repos_to_track` — list of repositories you want to back up. Leave `pushed_at` and `last_back_up` empty on first run.
---
