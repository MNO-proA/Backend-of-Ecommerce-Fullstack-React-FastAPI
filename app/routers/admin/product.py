import uuid
import aiofiles
import os
from fastapi import status, HTTPException, Depends, APIRouter, UploadFile
from sqlalchemy.orm import Session
from app.database import db_setup, models
from app import schemas
from . import admin_oauth2

router = APIRouter(
  prefix="/api/admin",
  tags=["Product"]
)

@router.post("/create-product", status_code=status.HTTP_201_CREATED, )
async def create_product( file: UploadFile, db: Session = Depends(db_setup.get_db), current_user: int = Depends(admin_oauth2.get_current_user) ):
    content = await file.read()
    if file.content_type not in ['image/jpeg', 'image/png']:
        raise HTTPException(status_code=406, detail="Only .jpeg or .png  files allowed")
    name_of_file, ext = os.path.splitext(file.filename)

    file_name = f'{uuid.uuid4().hex}{ext}'
    async with aiofiles.open(os.path.join('app/static',file_name), "wb") as f:
        await f.write(content)
    return {"file_name" : file_name}