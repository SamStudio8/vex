from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from vex import crud, models, schemas
from vex.database import SessionLocal, engine

app = FastAPI()

# Magic dependency https://fastapi.tiangolo.com/tutorial/sql-databases/
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/variants/{pos}")
def list_position(pos: int, db: Session = Depends(get_db), alts: str = None):
    if alts:
        # Get sample names for variant(s) at a position
        return crud.samples_by_variantrecord(db, pos=pos, alts=alts.split(','))
    else:
        # Summarise a single position
        return crud.summarise_records_by_position(db, pos)

# Add to database
@app.post("/variants/", response_model=schemas.VariantRecord)
def create_variantrecord(varr: schemas.VariantRecordCreate, db: Session = Depends(get_db)):
    return crud.create_variantrecord(db=db, varr=varr)
