# app/routes/youtube.py
from fastapi import APIRouter
from app.scrapers.youtube_scraper import get_youtube_videos

router = APIRouter()

@router.get("/test-youtube")
def test_youtube():
    """Simple test endpoint to check YouTube scraper."""
    try:
        results = get_youtube_videos("AI")
        return {"status": "ok", "count": len(results), "data": results}
    except Exception as e:
        return {"status": "error", "message": str(e)}
