from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from app import oauth2, schemas
from .. database import get_db


router = APIRouter(
    tags=["Profile"]
    )


@router.post("/api/profile", status_code=status.HTTP_201_CREATED)
async def profile( db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return {"user":"profile"}