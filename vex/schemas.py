from typing import List, Optional

from pydantic import BaseModel

class VariantRecordBase(BaseModel):
    cogid: str
    position: int
    ref: str
    alt: str
    is_indel: bool

class VariantRecordCreate(VariantRecordBase):
    pass

class VariantRecord(VariantRecordBase):
    id: int

    class Config:
        orm_mode = True
