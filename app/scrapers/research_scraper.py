# fetches latest research papers related to a specific topic using arXiv API
import requests

# Function to get latest research papers based on a query (default "artificial intelligence")
def get_latest_papers(query):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5"
    response = requests.get(url)
    entries = response.text.split("<entry>")[1:]

    papers = []
    for entry in entries:
        title_start = entry.find("<title>") + 7
        title_end = entry.find("</title>")
        link_start = entry.find("<id>") + 4
        link_end = entry.find("</id>")
        title = entry[title_start:title_end].strip().replace("\n", " ")
        link = entry[link_start:link_end]
        papers.append({"title": title, "url": link})

    return papers # return a list of dictionaries containing title and url for each paper
