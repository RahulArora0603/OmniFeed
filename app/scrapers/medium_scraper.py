import feedparser
import urllib.parse

def get_medium_posts(query="artificial intelligence",limit=10):
    encoded_query = urllib.parse.quote(query)
    feed_url = f"https://medium.com/feed/tag/{encoded_query}"
    feed = feedparser.parse(feed_url)
    posts = [
        {
            "title": entry.title,
            "url": entry.link
        }
        for entry in feed.entries[:limit]
    ]
    return posts