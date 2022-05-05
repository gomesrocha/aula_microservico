from fastapi import FastAPI
from routers.apiv1 import router as v1api

app = FastAPI()
app.include_router(v1api, prefix="/v1", tags=["v1"])