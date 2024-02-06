import pytest

from base.api.posts import PostsClient
from utils.clients.http.builder import get_http_client


@pytest.fixture(scope='class')
def class_posts_client() -> PostsClient:
    client = get_http_client()

    return PostsClient(client=client)
