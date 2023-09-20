from pydantic import BaseModel


class LineBase(BaseModel):
    mood: str
    pickupline: str


class LineCreate(LineBase):
    pass

class Line(LineBase):
    id: int

    class Config:
        orm_mode = True