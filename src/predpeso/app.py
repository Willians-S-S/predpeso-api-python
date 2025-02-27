from fastapi import FastAPI
from predpeso.routes.user_router import user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def get_test():
    return {"message":"olá mundo"}