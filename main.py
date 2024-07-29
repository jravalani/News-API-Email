# to build an api app that will call a server and retrieve news from the same and then send a mail.

import requests
from send_mail import send_mail

api_key = "fef8a28df1bb4e4fbcc7aead3ee95f82"
url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"

request = requests.get(url)
content = request.json()

titles = [article['title'] for article in content['articles']]
authors = [article['author'] for article in content['articles']]

message = f"Subject: Daily News Update (Top Headlines)\n\nFrom: News API\n\n"

for i in range(len(titles)):
    author = authors[i] if authors[i] else "Unknown Author"
    message += f"{i + 1}. {titles[i]} by {author}\n"

print(message)

send_mail(message)
