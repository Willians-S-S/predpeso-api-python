from fastapi import FastAPI
from predpeso.routes.user_router import user_router
from predpeso.routes.farm_router import farm_router

app = FastAPI()

app.include_router(user_router)
app.include_router(farm_router)

@app.get("/")
def get_test():
    return {"message":"olá mundo"}