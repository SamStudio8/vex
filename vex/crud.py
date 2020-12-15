from sqlalchemy.orm import Session
from sqlalchemy import func # https://stackoverflow.com/a/4086229/2576437

from . import models, schemas

def summarise_records_by_position(db: Session, pos: int):
    return db.query(models.VariantRecord.alt, func.count(models.VariantRecord.alt)).filter(models.VariantRecord.position == pos).group_by(models.VariantRecord.alt).all()

def create_variantrecord(db: Session, varr: schemas.VariantRecordCreate):
    varr_obj = models.VariantRecord(**varr.dict())
    db.add(varr_obj)
    db.commit()
    db.refresh(varr_obj)
    return varr_obj
