import requests
from datetime import datetime
import os

def percent_of_year_passed():
    now = datetime.now()
    start_of_year = datetime(now.year, 1, 1)
    end_of_year = datetime(now.year + 1, 1, 1)
    return ((now - start_of_year).total_seconds() / (end_of_year - start_of_year).total_seconds()) * 100

def create_progress_bar(percentage, bar_length=40):
    # Using a block for filled part and a dot for unfilled
    filled_length = int(round(bar_length * percentage / 100))
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    return bar

def create_github_release(token, repo, tag_name, name, body):
    url = f"https://api.github.com/repos/{repo}/releases"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "tag_name": tag_name,
        "name": name,
        "body": body,
        "draft": False,
        "prerelease": False
    }
    response = requests.post(url, headers=headers, json=data)
    return response

if __name__ == "__main__":
    progress = percent_of_year_passed()
    token = os.getenv('GIT_TOKEN')
    repo = "YearProgress/YearProgress"
    tag_name = f"Progress-{datetime.now().strftime('%Y%m%d')}"
    name = f"{datetime.now().strftime('%Y-%m-%d')}"
    progress_percentage = percent_of_year_passed()
    progress_bar = create_progress_bar(progress_percentage)
    body = f"# Year Progress\n{name}\n{progress_bar} {progress_percentage:.2f}%"

    response = create_github_release(token, repo, tag_name, name, body)
    print(response.json())
