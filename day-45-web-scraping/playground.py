from bs4 import BeautifulSoup
import requests

# Global Variable(s)
target_website_url = "https://news.ycombinator.com/news"

# Access target website & retrieve a copy of the main page
response = requests.get(target_website_url)
y_combinator_main_page = response.text

# Prepare the contents of the web page for scrapping
soup = BeautifulSoup(y_combinator_main_page, "html.parser")

# Search all <a> tags with class attribute of titlelink
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

# Retrieve individual title text & URL and save to corresponding lists
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.get("href")
    article_links.append(link)

# Retrieve individual upvote score
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# Retrieve the title & URL of the article with the highest upvote score
highest_upvote_index = article_upvotes.index(max(article_upvotes))
print(article_texts[highest_upvote_index])
print(article_links[highest_upvote_index])
