from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database, schemas, models, utils, oauth2
from sqlalchemy.orm import Session


router = APIRouter(tags=["Authentication"])

@router.post("/api/signin", response_model= schemas.User_Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    user = db.query(models.User).filter(user_credentials.username == models.User.email).first()

    print(user.role == 'user')

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credential")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credential")
    
    access_token = oauth2.create_access_token(
        data={"user_id":user.id})
    return {"user_access_token": access_token, "token_type": "bearer"}
