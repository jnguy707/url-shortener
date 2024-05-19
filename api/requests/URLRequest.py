from typing import Optional
from pydantic import BaseModel, HttpUrl

class URLRequest(BaseModel):
    url: HttpUrl
    custom_short_id: Optional[str] = None
