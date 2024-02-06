import requests
import typing
import allure
from settings import base_settings


class HTTPClient:
    BASE_URL = base_settings.api_url
    print(BASE_URL)

    @allure.step('Making GET request to "{url}"')
    def get(
        self,
        url: str,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        cookies: typing.Optional[typing.Dict[str, typing.Any]] = None,
        auth: typing.Optional[typing.Tuple[str, str]] = None,
        timeout: typing.Optional[typing.Union[float, tuple]] = None
    ) -> requests.Response:
        full_url = f"{self.BASE_URL}/{url}"
        return requests.get(
            url=full_url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            timeout=timeout
        )

    @allure.step('Making POST request to "{url}"')
    def post(
        self,
        url: str,
        data: typing.Optional[typing.Union[typing.Dict[str, typing.Any], str]] = None,
        json: typing.Optional[typing.Any] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        cookies: typing.Optional[typing.Dict[str, typing.Any]] = None,
        auth: typing.Optional[typing.Tuple[str, str]] = None,
        timeout: typing.Optional[typing.Union[float, tuple]] = None
    ) -> requests.Response:
        full_url = f"{self.BASE_URL}/{url}"
        return requests.post(
            url=full_url,
            data=data,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            timeout=timeout
        )

    @allure.step('Making PATCH request to "{url}"')
    def put(
            self,
            url: str,
            data: typing.Optional[typing.Union[typing.Dict[str, typing.Any], str]] = None,
            json: typing.Optional[typing.Any] = None,
            params: typing.Optional[typing.Dict[str, typing.Any]] = None,
            headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
            cookies: typing.Optional[typing.Dict[str, typing.Any]] = None,
            auth: typing.Optional[typing.Tuple[str, str]] = None,
            timeout: typing.Optional[typing.Union[float, tuple]] = None
    ) -> requests.Response:
        full_url = f"{self.BASE_URL}/{url}"
        return requests.patch(
            url=full_url,
            data=data,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            timeout=timeout
        )

    @allure.step('Making PATCH request to "{url}"')
    def patch(
        self,
        url: str,
        data: typing.Optional[typing.Union[typing.Dict[str, typing.Any], str]] = None,
        json: typing.Optional[typing.Any] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        cookies: typing.Optional[typing.Dict[str, typing.Any]] = None,
        auth: typing.Optional[typing.Tuple[str, str]] = None,
        timeout: typing.Optional[typing.Union[float, tuple]] = None
    ) -> requests.Response:
        full_url = f"{self.BASE_URL}/{url}"
        return requests.patch(
            url=full_url,
            data=data,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            timeout=timeout
        )

    @allure.step('Making DELETE request to "{url}"')
    def delete(
        self,
        url: str,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = None,
        cookies: typing.Optional[typing.Dict[str, typing.Any]] = None,
        auth: typing.Optional[typing.Tuple[str, str]] = None,
        timeout: typing.Optional[typing.Union[float, tuple]] = None
    ) -> requests.Response:
        full_url = f"{self.BASE_URL}/{url}"
        return requests.delete(
            url=full_url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
            timeout=timeout
        )


class APIClient:
    def __init__(self, client: HTTPClient) -> None:
        self._client = client

    @property
    def client(self) -> HTTPClient:
        return self._client
