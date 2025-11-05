# fetches latest Reddit posts related to a specific topic using PRAW (Python Reddit API Wrapper)
import praw
from app.config import REDDIT_CLIENT_ID
from app.config import REDDIT_CLIENT_SECRET
from app.config import REDDIT_USER_AGENT

# Function to get Reddit posts based on a query (default "artificial intelligence")
def get_reddit_posts(query="artificial intelligence"):
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )
    # Search for posts in all subreddits matching the query, sorted by relevance, limited to 5 results
    posts = []
    for submission in reddit.subreddit('all').search(query, sort="relevance", limit=10):
        posts.append({
            "title": submission.title,
            "url": submission.url,
            "image": submission.thumbnail if submission.thumbnail and submission.thumbnail.startswith("http") else None,
            "upvotes": submission.score
        })
    return posts # return a list of dictionaries containing title, url, image, and upvotes for each post
