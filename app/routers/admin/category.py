from fastapi import status, HTTPException, Depends, APIRouter
from app.database import db_setup, models
from app import schemas, utils
from sqlalchemy.orm import Session
from slugify import slugify
from app.database import db_setup
from typing import List
from . import admin_oauth2


router = APIRouter(
  prefix="/api/admin",
  tags=["Category"]
)

def getCatAndSubcat(categories, parentId:int = None):
  categoryList = []
  if(parentId == None):
    category = filter(lambda cat: cat.parentId == None, categories)
  else:
    category = filter(lambda cat: cat.parentId == parentId, categories)
  for cate in category:
    categoryList.append({
      "id": cate.id,
      "name": cate.name,
      "slug": cate.slug,
      "created_at":cate.created_at,
      "updated_at":cate.updated_at,
      "children": getCatAndSubcat(categories, cate.id)
    })
  return categoryList

# CREATE CATEGORIES
@router.post("/createCategory", status_code=status.HTTP_201_CREATED)
async def category(category:schemas.Category, db: Session = Depends(db_setup.get_db), current_user: int = Depends(admin_oauth2.get_current_user) ):
  category.slug = slugify(category.slug)
  new_cat = models.Category(**category.model_dump())
  db.add(new_cat)
  db.commit()
  db.refresh(new_cat)
  cat_object = {
    "id": new_cat.id,
    "name": new_cat.name,
    "slug": new_cat.slug,
    "created_at": new_cat.created_at
    }
  return {"category": cat_object}


# GET ALL CATEGORIES
@router.get("/getCategory", response_model=None)
async def getCategory(db: Session = Depends(db_setup.get_db), current_user: int = Depends(admin_oauth2.get_current_user)):
  categories = db.query(models.Category).all()

  if categories == None:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"There are no categories")
  
  categoryList = getCatAndSubcat(categories)
  return {"categoryList": categoryList}