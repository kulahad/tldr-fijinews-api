from typing import Optional
from enum import Enum
from beanie import Document, PydanticObjectId, Link
from pydantic import Field, BaseModel


class News(Document):
    id: str
    title: str
    summary: str
    article_url: str
    image_url: str
    publish_time: str
    source: str
