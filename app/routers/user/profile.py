from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from app import schemas
from app.database.db_setup import get_db
from app.routers.user import oauth2


router = APIRouter(
    tags=["Profile"]
    )


@router.post("/api/profile", status_code=status.HTTP_201_CREATED)
async def profile( db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    return {"user":"profile"}