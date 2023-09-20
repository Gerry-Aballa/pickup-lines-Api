import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app import api, schemas, models

from app.dependencies.database import SessionLocal, engine

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
    return {"message": "Hello Python"}


# @app.post("/lines/")  # Add pickuplines to the database
# def create_line(line: Line):
#     db = SessionLocal()
#     db.add(line)
#     db.commit()
#     db.refresh(line)
#     db.close()
#     return line


@app.get("/lines/random", response_model=schemas.Line)  # Return a random pickupline from the database
def random_line(db: Session = Depends(db_connection)):
    random_line = api.get_random_pickupline(db)
    if random_line is None:
        raise HTTPException(status_code=404, detail="No pickuplines found")
    return random_line


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)