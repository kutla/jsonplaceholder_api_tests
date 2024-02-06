from enum import Enum


class APIRoutes(str, Enum):
    POSTS = '/posts'

    def __str__(self) -> str:
        return self.value
