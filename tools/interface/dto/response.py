from typing import Any
from pydantic import BaseModel


class ToolResponse(BaseModel):
    response: Any
