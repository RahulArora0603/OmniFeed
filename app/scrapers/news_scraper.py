# fetches latest news articles related to a specific topic using NewsAPI
import requests # import the requests library to make HTTP requests
from app.config import NEWS_API_KEY

# Function to get the latest news articles based on a query (default "artificial intelligence")
def get_latest_news(query="artificial intelligence"):
    api_key = NEWS_API_KEY
    page = 1
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&"
        f"sortBy=publishedAt&"
        f"pageSize=5&"
        f"page={page}&"
        f"apiKey={api_key}"
    )
    response = requests.get(url) # make a GET request to the NewsAPI endpoint
    articles = response.json().get("articles", []) # parse the JSON response to extract articles

    # placeholder image if article image is None
    placeholder_image = "C:/Users/pc/Desktop/AI Pulse/app/static/pngtree-science-and-technology-future-high-tech-light-background-sci-fi-picture-image_2247992.jpg"
    news_list = []
    for article in articles:
        news_list.append({
            "title": article["title"],
            "url": article["url"],
            "image": article["urlToImage"]
        })
    return news_list # return a list of dictionaries containing title, url, and image for each article
