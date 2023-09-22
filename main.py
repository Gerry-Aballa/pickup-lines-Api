from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import uvicorn

from app import api, schemas, models

from app.dependencies.database import SessionLocal, engine

from typing import List



models.Base.metadata.create_all(bind=engine)

# Create a FastAPI app instance
app = FastAPI()


def db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create API endpoints

@app.get("/")
async def root():
    return {"Hello!": "This is a pickup lines API utilizing FastApi! Add /docs at the url to try this API "}


# @app.post("/lines/", response_model=List[schemas.Line])  # Add pickuplines to the database
# def create_line(lines: List[schemas.LineCreate], db: Session = Depends(db_connection)):
#     return [api.create_pickupline(db=db, line=line) for line in lines]


@app.get("/lines/random", response_model=schemas.Line)  # Return a random pickupline from the database
def random_line(db: Session = Depends(db_connection)):
    random_line = api.get_random_pickupline(db)
    if random_line is None:
        raise HTTPException(status_code=404, detail="No pickuplines found")
    return random_line


if __name__ == "__main__":
   
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
   