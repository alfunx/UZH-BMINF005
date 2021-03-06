# Empirical Analysis of Cloud Functions Metadata and Code

_Note:_ Check and adjust the paths in the shell scripts first.

## autocontents

We use the `autocontents.py` script to fetch data from
[aws.amazon.con](https://aws.amazon.com/) and from
[github.com](https://github.com). This script is executed by our server
once every day.

## Git repositories

To retrieve the URLs of all lambda functions available on Github, use the script
`get-git-urls.sh`. It requires an `autocontents.csv` file to extract all valid
Github URLs. Use it as follows:

```bash
./get-git-urls.sh /path/to/autocontents.sh
```

Next, we clone all Git repositories to analyze the code using tools and manual
review. Using the `git-urls.out.csv` generated by the `get-git-urls.sh` script,
we clone all repositories. Run the `clone-git-repos.sh` script to clone all
repositories to the specified directory.

## jshint

We use `jshint` (version: `2.9.6`) to analyze JavaScript code. Execute the
`run-jshint.sh` script to run `jshint` on all Git repositories in the specified
directory.

## pylint

We use `pylint` (version: `2.2.2`) to analyze Python code. Execute the
`run-pylint.sh` script to run `pylint` on all Git repositories in the specified
directory.
