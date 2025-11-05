from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse # HTMLResponse for rendering HTML templates
from fastapi.responses import FileResponse
from fastapi.params import Query
from fastapi.responses import JSONResponse
# Import individual scrapers
from .scrapers.reddit_scraper import get_reddit_posts
from .scrapers.medium_scraper import get_medium_posts
from .scrapers.youtube_scraper import get_youtube_videos
from .scrapers.news_scraper import get_latest_news
from .scrapers.research_scraper import get_latest_papers
from app.router import youtube_route

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(youtube_route.router)

@app.get("/")
def home(request: Request):
    return FileResponse("app/templates/new_index.html")

@app.get("/reddit") 
def reddit_posts(query: str = Query("artificial intelligence")):
    data = get_reddit_posts(query)
    return JSONResponse(content=data)

@app.get("/medium")
def medium_feed(query: str = Query("artificial intelligence")):
    data = get_medium_posts(query)
    return data

@app.get("/youtube")
def youtube_feed(query: str = Query("artificial intelligence")):
    data = get_youtube_videos(query)
    return data

@app.get("/news")
def news_feed(query: str = Query("artificial intelligence")):
    data = get_latest_news(query)
    return data

@app.get("/researchpapers")
def research_papers_feed(query: str = Query("artificial intelligence")):
    data = get_latest_papers(query)
    return data
