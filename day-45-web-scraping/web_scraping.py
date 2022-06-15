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

# To find all instances of the <a> tag
all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # To retrieve the text embedded within the <a> tag
    print(tag.getText())

    # To access the value of an attribute of the tag
    print(tag.get("href"))

# To access a tag by their attribute name
heading = soup.find(name="h1", id="name")
print(heading)

# To access a tag by their class name
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
# To access the text/content of the tag
print(section_heading.getText())

# To target a specific 1at matching embedded tag using a CSS selector
company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

# To target all elements by their class name using a CSS selector
heading = soup.find(name="h3", class_="heading")
print(heading.getText())
