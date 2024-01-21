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
            print("[-] Original repository")
        else:
            print("[-] No repositories:")
    else:
        print("[-] Error")
except requests.exceptions.ConnectionError:
    print("[-] Check the internet and try again")
except Exception as error:
    print("[-] Unknown error : " + error)
