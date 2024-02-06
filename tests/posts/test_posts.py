import json
from http import HTTPStatus

import allure
import pytest
from assertpy import assert_that

from base.api.posts import PostsClient
from models.posts import (DefaultPost, DefaultPostsList)
from utils.assertions.schema import validate_schema


@pytest.mark.posts
@allure.feature('Posts')
@allure.story('Posts API')
class TestPosts:
    @allure.title('Get posts')
    def test_get_all_posts(self, class_posts_client: PostsClient):
        response = class_posts_client.get_all_posts_api()
        json_response = response.json()
        with allure.step(f"Check that status is {HTTPStatus.OK}"):
            assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
        validate_schema(json_response, DefaultPostsList.model_json_schema())

    @allure.title('Get post')
    def test_get_post(self, class_posts_client: PostsClient):
        post_id = 1
        expected_dict = {
            "userId": 1,
            "id": 1,
            "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
            "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut"
                    " quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
        response = class_posts_client.get_post_api(post_id=post_id)
        json_response = response.json()
        with allure.step(f"Check that status is {HTTPStatus.OK}"):
            assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
        assert_that(json_response).is_equal_to(expected_dict)
        validate_schema(json_response, DefaultPost.model_json_schema())

    @allure.title('Create post')
    def test_create_posts(self, class_posts_client: PostsClient):
        post = {"userId": 1, "title": "test_title", "body": "test_body"}
        response = class_posts_client.create_post_api(payload=post)
        json_response = response.json()
        with allure.step(f"Check that status is {HTTPStatus.CREATED}"):
            assert_that(response.status_code).is_equal_to(HTTPStatus.CREATED)
        assert_that(post).is_subset_of(json_response)
        validate_schema(json_response, DefaultPost.model_json_schema())
