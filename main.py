import requests

def search_github(query):
    try:
        response = requests.get(f'https://api.github.com/search/repositories?q={query}')
        response.raise_for_status()

        data = response.json()
        items = data.get('items', [])

        if not items:
            print("No results found.")
        else:
            for item in items:
                #print(item)
                print(f"Repository URL www.github.com/{item['full_name']}, Description: {item['description']}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while connecting to the server: {e}")

if __name__ == "__main__":
    search_query = input("Enter the search term: ")
    search_github(search_query)

print("Copyright © 2024 - Ahmed Negm")
