from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app import database, schemas, models, utils 
from app.routers.admin import admin_oauth2
from sqlalchemy.orm import Session


router = APIRouter(tags=["Admin Authentication"])

@router.post("/api/admin/signin", response_model= schemas.Admin_Token)
def login(admin_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    admin = db.query(models.User).filter(admin_credentials.username == models.User.email).first()

    if not admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credential")
    
    if admin.role == 'user':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Access denied")

    if not utils.verify(admin_credentials.password, admin.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credential")
    
    access_token = admin_oauth2.create_access_token(
        data={"admin_id":admin.id})
    return {"admin_access_token": access_token, "token_type": "bearer"}
