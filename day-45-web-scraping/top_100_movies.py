from bs4 import BeautifulSoup
import requests

# Global Variable(s)
target_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Retrieve webpage
response = requests.get(target_url)
html_file = response.text

# Scrap content from webpage
soup = BeautifulSoup(html_file, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

# Scrap movie title text
movie_titles = [movie.getText() for movie in all_movies]

# Reverse the order of movie titles from 100 to 1 into 1 to 100 using a slice operator
movies = movie_titles[::-1]

# Save created list into a text file
with open("movies.txt", "w") as file:
    # Loop through the content line by line and write each line to the text file
    for movie in movies:
        file.write(f"{movie}\n")
