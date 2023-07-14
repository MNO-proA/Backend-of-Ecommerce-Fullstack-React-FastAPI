from fastapi import status, HTTPException, Depends, APIRouter
from app import database, schemas, models, utils
from sqlalchemy.orm import Session


router = APIRouter(
  prefix="/api/admin",
  tags=["Admins"]
)

@router.post("/signup")
def register(admin: schemas.BaseAdmin, db: Session = Depends(database.get_db) ):
    admin_email = db.query(models.User.email).filter(models.User.email == admin.email).first()
    if admin_email:
      raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Admin already registered!")
    hashed_password = utils.hash(admin.password)
    admin.password = hashed_password
    create_admin = models.User(**admin.dict())
    db.add(create_admin)
    db.commit()
    db.refresh(create_admin)
    return {"message":"Admin created successfully...!"}