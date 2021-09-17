import requests
import json
import argparse

def fetchTargets():
    with open('config.txt', 'r') as file:
        content = file.read()
        return list(filter(None, content.split('\n')))

def latestRelease(repo: str, token: str):
    r = requests.get(f'https://api.github.com/repos/{repo}/releases', headers={'Authorization': token})
    results = r.json()
    parsed = next((x for x in results if x['prerelease'] is False), None)
    output = {}
    if(parsed is None):
        return output
    output['releaseUrl'] = parsed['html_url']
    output['releaseNotes'] = parsed['body']
    output['version'] = parsed['tag_name']
    return output

def repoInfo(repo: str, token: str):
    r = requests.get(f'https://api.github.com/repos/{repo}', headers={'Authorization': token})
    results = r.json()
    if('html_url' not in results):
        print(results) # Debug - were we rate limited?
        return {}
    return results['html_url']

def writeOutput(results: dict):
    json_object = json.dumps(results, indent = 4) 
    with open('output.json', 'w') as file:
        file.write(json_object)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help="GitHub Personal Access Token")
    args = parser.parse_args()
    if not args.token:
        print('Please retry with a GitHub PAT token specified with the `--token TOKEN` argument')
        return
    results = []
    for repository in fetchTargets():
        result = {}
        result['name'] = repository
        result['repoInfo'] = repoInfo(repository, args.token)
        result['releaseInfo'] = latestRelease(repository, args.token)
        results.append(result)
    writeOutput(results)

if __name__ == "__main__":
    main()