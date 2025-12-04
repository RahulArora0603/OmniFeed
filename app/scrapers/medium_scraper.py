import feedparser
import urllib.parse

def get_medium_posts(query="artificial intelligence",limit=10):
    try:

        encoded_query = urllib.parse.quote(query)
        feed_url = f"https://medium.com/feed/tag/{encoded_query}"
        feed = feedparser.parse(feed_url)
        posts = [
            {
                "name": "Medium",
                "title": entry.title,
                "url": entry.link
            }
            for entry in feed.entries[:limit]
        ]
        return posts
    except Exception as e:
        #print(f"An error occurred while fetching Medium posts: {e}")
        return [{"title": "Rate limit reached or temporary error", "url": "#"}]  # return an empty list in case of error