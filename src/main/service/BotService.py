import os

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
from src.main.config import db

# Select the collection
COLLECTION_SEARCH_HISTORY = os.getenv('COLLECTION_SEARCH_HISTORY')
collection = db[COLLECTION_SEARCH_HISTORY]
collection.create_index([('searchString', 'text')])

search_str = "!google"
recent_str = "!recent"


def search_results(query):
    query = str(query).lower()
    results = []
    if query.find(search_str) != -1:
        results = get_search_results(query)
    elif query.find(recent_str) != -1:
        results = get_recent_search(query)
    return results


def get_search_results(query):
    query = query.replace(search_str, "").strip()
    doc = {"searchString": query}
    if collection.count(doc) == 0:
        collection.insert(doc)
    results = []
    for j in search(query, tld="com", num=5, stop=5, pause=2):
        results.append(j)
    return results


def get_recent_search(query):
    query = query.replace(recent_str, "").strip()
    results = []
    for item in collection.find({"$text": {"$search": query}}, {"score": {"$meta": "textScore"}}):
        results.append(item['searchString'])
    # sort functionality is pending
    return results
