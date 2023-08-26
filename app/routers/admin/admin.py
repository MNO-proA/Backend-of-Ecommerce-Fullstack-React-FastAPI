from fastapi import status, HTTPException, Depends, APIRouter
from app.database import db_setup, models
from app import schemas, utils
from sqlalchemy.orm import Session


router = APIRouter(
  prefix="/api/admin",
  tags=["Admins"]
)

@router.post("/signup")
async def register(admin: schemas.BaseAdmin, db: Session = Depends(db_setup.get_db) ):
    admin_email = db.query(models.User.email).filter(models.User.email == admin.email).first()
    if admin_email:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Admin already registered!")
    hashed_password = utils.hash(admin.password)
    admin.password = hashed_password
    create_admin = models.User(**admin.model_dump())
    db.add(create_admin)
    db.commit()
    db.refresh(create_admin)
    return {"message":"Admin created successfully...!"}