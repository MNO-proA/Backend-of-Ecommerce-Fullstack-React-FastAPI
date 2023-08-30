from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.database import db_setup, models
from app import schemas, utils
from sqlalchemy.orm import Session

from app.routers.user import oauth2


router = APIRouter(tags=["User Authentication"])

@router.post("/api/signin", response_model= schemas.User_Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db_setup.get_db)):

    user = db.query(models.User).filter(user_credentials.username == models.User.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credential")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credential")
    
    access_token = oauth2.create_access_token(
        data={"user_id":user.id})
    return {"user_access_token": access_token, "token_type": "bearer"}
