# #Task 1 (7.1)
import requests
from typing import Dict, List
from dotenv import load_dotenv
import os


load_dotenv()

token = os.getenv("GITHUB_TOKEN")


def check_status_code(response: requests.Response):
    status_code = response.status_code
    if status_code == 200:
        return
    elif 400 <= status_code < 500:
        raise ValueError(f"Client Error: {status_code} - {response.text}")
    elif 500 <= status_code < 600:
        raise ValueError(f"Server Error: {status_code} - {response.text}")
    else:
        raise ValueError(f"Unexpected Error: {status_code} - {response.text}")


def get_repository_info(repo_name: str) -> Dict[str, str]:
    url = f"https://api.github.com/repos/{repo_name}" # URL GitHub API
    headers = {
        "Authorization": f"token {token}"
    }
    response = requests.get(url, headers=headers) # send GET to API github

    check_status_code(response)

    repo_data = response.json()
    if not repo_data:
        raise ValueError("Error: Empty data from GitHub API.")

    repo_info = {
        "Repository Name": repo_data.get("name"),
        "Owner": repo_data.get("owner", {}).get("login"),
        "Description": repo_data.get("description") or "empty",
        "License": repo_data.get("license", {}).get("name") if repo_data.get("license") else "not available",
        "Creation Date": repo_data.get("created_at")
    }
    return repo_info

def print_info(repo_info: Dict[str, str]):
    print(f"Repository Name: {repo_info['Repository Name']}\n"
          f"Owner: {repo_info['Owner']}\n"
          f"Description: {repo_info['Description']}\n"
          f"License: {repo_info['License']}\n"
          f"Creation Date: {repo_info['Creation Date']}")
    print()


#Task 2 (7.1)
def get_recent_commits(repo_name: str, commit_count: int) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo_name}/commits"
    headers = {
        "Authorization": f"token {token}"
    }
    response = requests.get(url, headers=headers)  # send request

    check_status_code(response)

    commits_data = response.json()
    if not commits_data:
        raise ValueError("Error: Empty data from GitHub API.")

    recent_commits = []
    for commit in commits_data[-commit_count:]: # five most recent commits
        commit_info = {
            "Message": commit["commit"]["message"],
            "Author": commit["commit"]["author"]["name"],
            "Date": commit["commit"]["author"]["date"],
            "Commit URL": commit["html_url"]
        }
        recent_commits.append(commit_info)

    return recent_commits

def print_commits(commits: List[Dict[str, str]]):
    for i, commit in enumerate(commits, 1):
        print(f"Commit {i}:\n"
              f"Commit Message: {commit['Message']}\n"
              f"Author: {commit['Author']}\n"
              f"Date: {commit['Date']}\n"
              f"Link to the commit on GitHub: {commit['Commit URL']}\n")


try:
    repo_info = get_repository_info("TetianaAbasova/new_calculator")
    print_info(repo_info)

    commit_count = 5
    commits = get_recent_commits("TetianaAbasova/new_calculator", commit_count)
    print_commits(commits)

except ValueError as e:
    print(e)