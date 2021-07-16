# scraping a website for the statistics of top 5  programming languages used by programmers in 2020 and representing them in a pie chart
# imports ----

from bs4 import BeautifulSoup as bs
import requests
import string
import matplotlib.pyplot as plt

# creating soup essentials----

url = "https://insights.stackoverflow.com/survey/2020#technology-most-loved-dreaded-and-wanted-languages-loved"

content = requests.get(url).text
soup = bs(content, 'lxml')

# finding the table --

div = soup.find('div', attrs={
                'name': "technology-most-loved-dreaded-and-wanted-languages-loved"})
rows = div.find_all('tr')[0:5]  # since we only need the top 5 languages

# all the text content within the tr tag
lst = [item.get_text() for item in rows]

# representing the percentage values and languages in different lists---


# func to be used for removing extra whitespaces and \n from the elements of the list
def func(x): return string.capwords(x)


values = list(map(func, lst))
# contains all the languages (list)
lang = list(map(lambda x: x.split(" ")[0], values))
# contains all the percentage (list)
percent = list(map(lambda x: x.split(" ")[1], values))

# print(lang, percent)

# pie chart representation---


# removing the % sign from all the values
def fun(y): return float(y.rstrip("%"))


# mapping the above function in the percent list
percent2 = list(map(fun, percent))
total = sum(percent2)

# pie chart representation---
E = [0, 0.1, 0.1, 0, 0]

plt.title("Programming languages used by programmers in 2020")

plt.pie(percent2, labels=lang, explode=E,
        autopct=lambda p: '{:.0f}%'.format(p * total / 100))  # '[FLAG][WIDTH].[PRECISION]type'
plt.show()
