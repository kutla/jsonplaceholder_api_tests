import allure
from requests import Response
import json

from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class PostsClient(APIClient):
    @allure.step(f"Getting all posts")
    def get_all_posts_api(self) -> Response:
        return self.client.get(APIRoutes.POSTS)

    @allure.step(f'Getting post')
    def get_post_api(self, post_id: int) -> Response:
        return self.client.get(f'{APIRoutes.POSTS}/{post_id}')

    @allure.step(f'Creating post')
    def create_post_api(self, payload) -> Response:
        print(json.dumps(payload))
        return self.client.post(url=f'{APIRoutes.POSTS}', json=payload)

    @allure.step(f'Updating post')
    def update_post_api(self, post_id: int, payload) -> Response:
        return self.client.get(f'{APIRoutes.POSTS}/{post_id}')

    @allure.step(f'Patching post')
    def patch_post_api(self, post_id: int, payload) -> Response:
        return self.client.get(f'{APIRoutes.POSTS}/{post_id}')

    @allure.step(f'Deleting post')
    def delete_post_api(self, post_id: int) -> Response:
        return self.client.get(f'{APIRoutes.POSTS}/{post_id}')
