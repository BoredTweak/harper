# Harper

Tool to fetch the latest releases in technologies.

## Prerequisites

- [Python][technology-main]

## Running the Service

- From the root directory run `py app.py`
- To test, run `curl -X GET "http://localhost:5000/tech?repo=vercel/next.js" -H 'token: YOUR_GITHUB_PAT_HERE'`

## Running Locally

- Create a [GitHub Personal Access Token][gh-token]. 
  - *NOTE - This token has no specific requirements. It simply provides basic authentication in order to increase the API rate limit.*
- Create a `config.txt` in the [configuration](./configuration) directory. A [`config.example.txt`](./configuration/config.example.txt) is provided for reference.
- From a terminal instance in this directory install dependencies by running `pip install -r requirements.txt`
- Run the application by running `py harper.py --token YOUR_GITHUB_PAT_HERE`
- The results are currently stored in an `output.json` file.

### Help

- To see available arguments run `python harper.py --help` from a terminal instance in this directory.

## Example Output

If leveraging a `config.txt` such as:
```txt
vercel/next.js
facebook/react
vuejs/vue
```

The generated `output.json` may look as follows:
```json
[
    {
        "name": "vercel/next.js",
        "repoInfo": "https://github.com/vercel/next.js",
        "releaseInfo": {
            "releaseUrl": "https://github.com/vercel/next.js/releases/tag/v11.1.2",
            "releaseNotes": "### Core Changes\r\n\r\n- chore: upgrade styled-jsx to 4.0.1: #28626\r\n- getServerSideProps should support props value as Promise: #28607\r\n- Ensure custom app regex is correct for Windows: #28631\r\n\r\n### Credits \r\n\r\nHuge thanks to @huozhi and @kara for helping!\r\n",
            "version": "v11.1.2",
            "publishDate": "2021-08-31T05:16:04Z"
        }
    },
    {
        "name": "facebook/react",
        "repoInfo": "https://github.com/facebook/react",
        "releaseInfo": {
            "releaseUrl": "https://github.com/facebook/react/releases/tag/v17.0.2",
            "releaseNotes": "### React DOM\r\n\r\n* Remove an unused dependency to address the [`SharedArrayBuffer` cross-origin isolation warning](https://developer.chrome.com/blog/enabling-shared-array-buffer/). ([@koba04](https://github.com/koba04) and [@bvaughn](https://github.com/bvaughn) in [#20831](https://github.com/facebook/react/pull/20831), [#20832](https://github.com/facebook/react/pull/20832), and [#20840](https://github.com/facebook/react/pull/20840))\r\n\r\n## Artifacts\r\n\r\n- react: https://unpkg.com/react@17.0.2/umd/\r\n- react-art: https://unpkg.com/react-art@17.0.2/umd/\r\n- react-dom: https://unpkg.com/react-dom@17.0.2/umd/\r\n- react-is: https://unpkg.com/react-is@17.0.2/umd/\r\n- react-test-renderer: https://unpkg.com/react-test-renderer@17.0.2/umd/\r\n- scheduler: https://unpkg.com/scheduler@0.20.2/umd/",
            "version": "v17.0.2",
            "publishDate": "2021-03-22T22:00:26Z"
        }
    },
    {
        "name": "vuejs/vue",
        "repoInfo": "https://github.com/vuejs/vue",
        "releaseInfo": {
            "releaseUrl": "https://github.com/vuejs/vue/releases/tag/v2.6.14",
            "releaseNotes": "### Bug Fixes\r\n\r\n* **types:** async Component types (#11906) c52427b, closes #11990\r\n* **v-slot:** fix scoped slot normalization combined with v-if (#12104) 38f71de, closes #12102\r\n\r\n\r\n### Features\r\n\r\n* **ssr:** vue-ssr-webpack-plugin compatible with webpack 5 (#12002) 80e7730, closes #11718\r\n\r\n\r\n\r\n",
            "version": "v2.6.14",
            "publishDate": "2021-06-07T09:56:25Z"
        }
    }
]
```

## Additional Reading

- [Requests Library](https://requests.kennethreitz.org/en/master/)
- [ArgParse Library](https://docs.python.org/3/library/argparse.html)

[technology-main]: https://www.python.org/downloads/
[gh-token]: https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token