from pydantic import BaseModel, Field
from typing import List, Optional

from .base import RealModel, DateTimeMixin, DBModelMixin, Author


class PostBase(RealModel):
    title: str
    caption: str
    body: str
    published: bool = True


class Post(DateTimeMixin, PostBase):
    author: Author
    slug: str


class PostDoc(DBModelMixin, Post):
    pass


class NewPost(PostBase):
    pass


class PostResponse(RealModel):
    post: Post


class PostListResponse(RealModel):
    posts: List[PostDoc]
    post_count: int = Field(..., alias="postCount")


class UpdatePost(RealModel):
    title: Optional[str] = None
    caption: Optional[str] = None
    body: Optional[str] = None
    published: Optional[bool] = True


class PostFilterParams(BaseModel):
    title: Optional[str] = None
