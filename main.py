from fastapi import FastAPI
from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate
from operations.router import router as router_operations
from tasks.router import router
from fastapi.middleware.cors import CORSMiddleware
from pages.router import router as router_pages
from fastapi.staticfiles import StaticFiles

app=FastAPI(title="Trading app")

app.mount('/static',StaticFiles(directory="static"),name="static")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(router_operations)
app.include_router(router)
app.include_router(router_pages)


origins = [
    "http://localhost:3000",
    "https://amazon.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","OPTIONS","DELETE","PATCH","PUT"],
    allow_headers=["Content_Type","Set-Cookie","Access-Control-Allow-Headers","Authorization"]
)



@app.get("/")
async def main():
    return {"message": "Hello World"}
