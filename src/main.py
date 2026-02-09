from fastapi import FastAPI
from src.api.Routes import router
app = FastAPI(
    title="ClassifyEat",
)
app.include_router(router)
