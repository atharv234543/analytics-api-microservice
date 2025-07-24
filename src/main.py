from contextlib import asynccontextmanager
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from api.db.session import init_db
from api.events import router as event_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    #before app startup
    init_db()
    #app cleanup
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_method=["*"],
    allow_headers=["*"],
)
app.include_router(event_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/healthz/")
def health_check_endpoint():
    return {"status": "ok"}