import requests
class JSONPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def fetch_posts(self):
        """Fetches a list of posts."""
        try:
            response = requests.get(f"{self.base_url}/posts")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error fetching posts:", e)
            return None
    def create_post(self, title, body, user_id):
        """Creates a new post."""
        payload = {"title": title, "body": body, "userId": user_id}
        try:
            response = requests.post(f"{self.base_url}/posts", json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error creating post:", e)
            return None
if __name__ == "__main__":
    client = JSONPlaceholderClient()
    posts = client.fetch_posts()
    if posts:
        print("Fetched posts:", posts[:2])
        new_post = client.create_post("Sample Title", "Sample body content", 1)
        if new_post:
            print("Created post:", new_post)
