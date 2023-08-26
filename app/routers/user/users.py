from fastapi import status, HTTPException, Depends, APIRouter
from app.database import db_setup, models
from app import schemas, utils
from sqlalchemy.orm import Session


router = APIRouter(
  prefix="/api",
  tags=["Users"]
)

@router.post("/signup")
async def register(user: schemas.BaseUsers, db: Session = Depends(db_setup.get_db) ):
    user_email = db.query(models.User.email).filter(models.User.email == user.email).first()
    if user_email:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"User already registered!")
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    create_user = models.User(**user.model_dump())
    db.add(create_user)
    db.commit()
    db.refresh(create_user)
    return {"message":"User created successfully...!"}