from fastapi import APIRouter, Depends
from slugify import slugify
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from .crud import get_all_posts, create_post, get_post_by_slug
from ..database.models import NewPost, PostListResponse, PostDoc
from ..database.utils import get_database, AIOMC

router = APIRouter()


@router.get("/posts", response_model=PostListResponse)
async def get_posts(db: AIOMC = Depends(get_database)):
    posts = await get_all_posts(db)
    return PostListResponse(posts=posts, post_count=len(posts))


@router.post("/posts", response_model=PostDoc, status_code=HTTP_201_CREATED)
async def new_post(post: NewPost, db: AIOMC = Depends(get_database)):
    slug = slugify(post.title)
    exists = await get_post_by_slug(slug, db)

    if not exists:
        doc = await create_post(post, slug, db)
        return doc

    raise HTTPException(
        status_code=HTTP_400_BAD_REQUEST,
        detail=f"Post with slug '{slug}' already exists"
    )


@router.get("/posts/{slug}", response_model=PostDoc)
async def post_details(slug: str, db: AIOMC = Depends(get_database)):
    doc = await get_post_by_slug(slug, db)

    if not doc:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Post with slug '{slug}' not found",
        )

    return doc


@router.patch("/posts/{slug}")
async def update_post(slug: str):
    return {"post": {}}


@router.delete("/posts/{slug}", status_code=HTTP_204_NO_CONTENT)
async def delete_post(slug: str, db: AIOMC = Depends(get_database)):
    return {"message": "success"}
