from fastapi import FastAPI
from . routers.user import users, auth, profile
from .database import models
from .database.db_setup import engine
from .routers.admin import admin, admin_auth, admin_profile, category, product

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Fast API Ecommerce",
    description="Ecommerce API for online business.",
    version="0.0.1",
    contact={
        "name": "Michael Nana Ofosu",
        "email": "Michaelnanaofosu@gmail.com",
    },
    license_info={
        "name": "MIT",
    },
)


app.include_router(users.router)
app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(admin.router)
app.include_router(admin_auth.router)
app.include_router(admin_profile.router)
app.include_router(category.router)
app.include_router(product.router)







