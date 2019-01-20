import os
from errors import EnvironmentArgError
from github import Github

if __name__ == "__main__":
    TOKEN = os.environ.get("GITHUB_API_TOKEN", None)
    if TOKEN:
        G = Github(TOKEN)
    else:
        raise EnvironmentArgError(
            "Could not find GITHUB_API_TOKEN in"
            + " environment. Please set to access API!"
        )
