from fastapi import APIRouter
from app.api.v1 import (
    products,
    stores,
    categories,
    countries,
    cities,
    users,
)


api_router = APIRouter()


# Register sub-routers under a versioned path
api_router.include_router(products.router, prefix="/products", tags=["Products"])
api_router.include_router(stores.router, prefix="/stores", tags=["Stores"])
api_router.include_router(categories.router, prefix="/categories", tags=["Categories"])
api_router.include_router(countries.router, prefix="/countries", tags=["Countries"])
api_router.include_router(cities.router, prefix="/cities", tags=["Cities"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])