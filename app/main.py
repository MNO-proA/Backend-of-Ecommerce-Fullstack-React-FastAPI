from fastapi import FastAPI
from. routers import users, auth, profile
from . import models
from .database import engine
from .routers.admin import admin, admin_auth, admin_profile, category

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(admin.router)
app.include_router(admin_auth.router)
app.include_router(admin_profile.router)
app.include_router(category.router)







