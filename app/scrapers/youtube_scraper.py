# fetches latest YouTube videos related to a specific topic using youtubesearchpython
from youtubesearchpython import VideosSearch

# Function to get YouTube videos based on a query (default "artificial intelligence")
def get_youtube_videos(query = "artificial intelligence"):
    videos_search = VideosSearch(query, limit=10)
    results = videos_search.result()["result"]

    video_list = []
    for video in results:
        video_list.append({
            "title": video["title"],
            "url": video["link"],
            "image": video["thumbnails"][0]["url"]
        })
    return video_list # return a list of dictionaries containing title, url, and image for each video