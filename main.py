import requests

RepositoryName = input("[~] Repository name : ")

URL = f"https://api.github.com/search/repositories?q={RepositoryName}&type=public"

try:
    request = requests.get(URL)
    if request.status_code == 200:
        repositories = request.json()["items"]
        if repositories:
            for repo in repositories:
                print(repo['full_name']+ " | " + repo['html_url'])
            print("[•] Don't forget to put a star to the repository on GitHub.")
        else:
            print("[•] Error. No repository found")
    else:
        print("[•] Error. Unknown")
except requests.exceptions.ConnectionError:
    print("[•] Please check your internet connection and try again")
except Exception as error:
    print("[•] Error. " + str(error))
