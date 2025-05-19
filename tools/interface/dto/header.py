from pydantic import BaseModel


class CustomHeader(BaseModel):
    user_token: str
    request_id: str
