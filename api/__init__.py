from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from extractors import fijivillage
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from contextlib import asynccontextmanager
from beanie.operators import In
from models import News
import os
from dotenv import load_dotenv
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DBNAME = os.getenv("MONGODB_DBNAME")


async def init():
    client = AsyncIOMotorClient(MONGODB_URI)
    await init_beanie(database=client[MONGODB_DBNAME], document_models=[News])


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="tldr-fijinews-api",
        version="0.1.0",
        summary="A streamlined API for aggregating and summarizing news from Fijian sources.",
        description="Get concise, up-to-date local news at your fingertips.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.get("/", include_in_schema=False)
async def main():
    return RedirectResponse(app.docs_url)


@app.get("/news")
async def news():
    # get data from db
    news = await News.find_all().to_list()
    return news


@app.post("/grabnews")
async def grabnews():
    # store data in db
    news = fijivillage()
    newslist = [News(**item) for item in news.htmlparser()]
    newarticles = 0
    duplicatearticles = 0

    for news in newslist:
        exists = await News.get(news.id)
        if bool(exists):
            print("Article already exits in db")
            duplicatearticles += 1
        else:
            await News.insert(news)
            newarticles += 1

    return {
        "message": f"{newarticles} new articles added, {duplicatearticles} duplicate articles ignored."
    }
