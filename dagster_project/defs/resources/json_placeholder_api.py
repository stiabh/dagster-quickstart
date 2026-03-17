import dagster as dg
import requests


class JsonPlaceholderApi(dg.ConfigurableResource):
    api_key: str  # not used

    @property
    def base_url(self) -> str:
        return "https://jsonplaceholder.typicode.com/"

    def _get_response_json(self, endpoint: str) -> dict | list[dict]:
        response = requests.get(url=f"{self.base_url}/{endpoint}")
        response.raise_for_status()

        return response.json()

    def get_posts(self):
        endpoint = "posts"
        return self._get_response_json(endpoint)
