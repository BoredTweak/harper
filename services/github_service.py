
from models import Release, Notification
import requests


class GitHubService:
    def __init__(self, token: str):
        self.base_api_url = f'https://api.github.com'
        self.token = token

    def latestRelease(self, repo: str) -> Release:
        r = requests.get(f'{self.base_api_url}/repos/{repo}/releases', headers={'Authorization': self.token})
        results = r.json()
        parsed = next((x for x in results if x['prerelease'] is False), None)
        output = Release()
        if(parsed is None):
            return output
        output.releaseUrl = parsed['html_url']
        output.releaseNotes = parsed['body']
        output.version = parsed['tag_name']
        return output

    def generateNotification(self, repo: str) -> Notification:
        r = requests.get(f'{self.base_api_url}/repos/{repo}', headers={'Authorization': self.token})
        results = r.json()
        output = Notification()
        output.name = repo
        if('html_url' not in results):
            print(results) # Debug - were we rate limited?
            return output
        output.repoInfo = results['html_url']
        output.releaseInfo = self.latestRelease(repo)
        return output
