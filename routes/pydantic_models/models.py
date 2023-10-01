from pydantic import BaseModel


class Remind(BaseModel):
    today: bool = False
    list_all: bool = False
    date: str = None
    name: str = None
