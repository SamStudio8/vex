from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base

class VariantRecord(Base):
    __tablename__ = "variantrecords"

    id = Column(Integer, primary_key=True, index=True)
    cogid = Column(String, index=True)
    position = Column(Integer, index=True)
    ref = Column(String)
    alt = Column(String)
    is_indel = Column(Boolean, default=False)
