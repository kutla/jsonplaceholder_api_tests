from pydantic import BaseModel, Field, RootModel
from typing import TypedDict


class DefaultPost(BaseModel):
    id: int = Field()
    user_id: int = Field(alias='userId')
    title: str | None = Field()
    body: str | None = Field()


class DefaultPostsList(RootModel):
    root: list[DefaultPost]


class PostsDict(TypedDict):
    id: int
    userId: int
    title: str
