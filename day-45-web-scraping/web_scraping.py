from bs4 import BeautifulSoup
# import lxml

# Constant Variable(s)
FILE_PATH = "website.html"

with open(FILE_PATH, "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# Returns the <title> tag
print(soup.title)

# Returns the name of the HTML tag
print(soup.title.name)

# Returns the string content of the <title> tag
print(soup.title.string)

# Returns a properly indented content of the soup object
print(soup.prettify())

# Returns the 1st <a> tag
print(soup.a)

# Returns the 1st <li> tag
print(soup.li)

# Returns the 1st <p> tag
print(soup.p)
