from pydantic import BaseModel

class UserMark(BaseModel):
    user_id: int
    mark: str