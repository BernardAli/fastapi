from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # Default
    # rating: Optional[int] = None    # Optional