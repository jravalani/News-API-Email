# to build an api app that will call a server and retrieve news from the same and then send a mail.

import requests

api_key = "fef8a28df1bb4e4fbcc7aead3ee95f82"
url = ("https://newsapi.org/v2/everything?q=tesla&" \
       "from=2024-06-28&sortBy=publishedAt&" \
       "apiKey=fef8a28df1bb4e4fbcc7aead3ee95f82")

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    title = article['title']
    description = article['description']
    print(f"Title: {title}, \n Description: {description}")
