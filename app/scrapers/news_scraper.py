# fetches latest news articles related to a specific topic using NewsAPI
import requests # import the requests library to make HTTP requests
from app.config import NEWS_API_KEY

# Function to get the latest news articles based on a query (default "artificial intelligence")
def get_latest_news(query="artificial intelligence"):
    try:

        api_key = NEWS_API_KEY
        page = 1
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={query}&"
            f"sortBy=publishedAt&"
            f"pageSize=10&"
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
                "name": "NewsAPI",
                "title": article["title"],
                "url": article["url"],
                "image": article["urlToImage"]
            })
        return news_list # return a list of dictionaries containing title, url, and image for each article
    except Exception as e:
        #print(f"An error occurred while fetching news articles: {e}")
        return [{"title": "Rate limit reached or temporary error", "url": "#", "image": None}]  # return an empty list in case of error