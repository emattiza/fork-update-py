import os
from errors import EnvironmentArgError
from github import Github


def print_repos(ghub):
    for repo in ghub.get_user().get_repos():
        print(repo.name)
    print(repo)


if __name__ == "__main__":
    TOKEN = os.environ.get("GITHUB_API_TOKEN", None)
    if TOKEN:
        G = Github(TOKEN)
    else:
        raise EnvironmentArgError(
            "Could not find GITHUB_API_TOKEN in"
            + " environment. Please set to access API!"
        )
    if G:
        print_repos(G)
