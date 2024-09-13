from fastapi import FastAPI
from extractors import fijivillage
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from contextlib import asynccontextmanager
from beanie.operators import In
from models import News
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DBNAME = os.getenv('MONGODB_DBNAME')


async def init():
    client = AsyncIOMotorClient(MONGODB_URI)
    await init_beanie(database=client[MONGODB_DBNAME], document_models=[News])


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def main():
    return "Welcome to TLDR Fiji news api, check /docs for more!"

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

    return {"message": f"{newarticles} new articles added, {duplicatearticles} duplicate articles ignored."}
    