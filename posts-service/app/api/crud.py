from datetime import datetime

from bson import ObjectId

from ..config.database import posts_coll, posts_db
from ..database.models import NewPost, PostDoc
from ..database.models.base import Author
from ..database.utils import AIOMC


async def get_all_posts(db: AIOMC):
    cursor = db[posts_db][posts_coll].find({'published': True})
    return [PostDoc(**doc, created_at=ObjectId(doc['_id']).generation_time) async for doc in cursor]


async def get_post_by_slug(slug: str, db: AIOMC):
    doc = await db[posts_db][posts_coll].find_one({'published': True, 'slug': slug})
    return PostDoc(**doc, created_at=ObjectId(doc['_id']).generation_time)


async def create_post(post: NewPost, slug: str, db: AIOMC):
    post_doc = post.dict()
    post_doc['slug'] = slug
    post_doc['author'] = Author().dict()
    post_doc['updated_at'] = datetime.now()

    result = await db[posts_db][posts_coll].insert_one(post_doc)
    doc = await db[posts_db][posts_coll].find_one({'_id': result.inserted_id})
    return PostDoc(**doc, created_at=ObjectId(doc['_id']).generation_time)


async def update_post_by_slug():
    pass


async def delete_post_by_slug():
    pass
