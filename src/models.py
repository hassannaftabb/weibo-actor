from pydantic import BaseModel, Field
from typing import List, Optional

class InputModel(BaseModel):
    keywords: List[str] = Field(default=["护肤", "健身", "旅行", "穿搭", "美食"])
    max_pages: int = Field(default=3, ge=1, le=10)
    concurrency: int = Field(default=5, ge=1, le=20)

class PostModel(BaseModel):
    post_id: str
    text_raw: str
    created_at: str
    likes: int
    reposts: int
    comments: int
    pics: List[str]
    author_id: str
    author_name: str
    verified: bool
    followers: int
    hashtags: Optional[List[str]] = []