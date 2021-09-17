# Harper

Tool to fetch the latest releases in technologies.

## Prerequisites

- [Python][technology-main]

## Running Locally

- Create a [GitHub Personal Access Token][gh-token]. 
  - *NOTE - This token has no specific requirements. It simply provides basic authentication in order to increase the API rate limit.*
- Create a `config.txt` in the [configuration](./configuration) directory. A [`config.example.txt`](./configuration/config.example.txt) is provided for reference.
- From a terminal instance in this directory install dependencies by running `pip install -r requirements.txt`
- Run the application by running `py harper.py --token YOUR_GITHUB_PAT_HERE`
- The results are currently stored in an `output.json` file.

## Additional Reading

- [Requests Library](https://requests.kennethreitz.org/en/master/)

[technology-main]: https://www.python.org/downloads/
[gh-token]: https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token