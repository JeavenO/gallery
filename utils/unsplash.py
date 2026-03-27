import requests

ACCESS_KEY = "06dvJ6N0laU6WZEiZc1X5ZeHO9ceft9TQ25yJT6jaVs"

def get_photos(category, per_page=9):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": category,
        "per_page": per_page,
        "client_id": ACCESS_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []
    data = response.json()
    return [item["urls"]["small"] for item in data.get("results", [])]


