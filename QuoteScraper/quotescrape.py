import random

import requests
from bs4 import BeautifulSoup


response = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(response.text, "html.parser")
short_url = "http://quotes.toscrape.com"

quote_list = []
while True:
    page_quotes = soup.findAll(class_="quote")
    for whole_quote in page_quotes:
        quote = whole_quote.find(class_="text").get_text()
        author = whole_quote.find(class_="author").get_text()
        link = whole_quote.find("a")["href"]
        quote_list.append([quote, author, link])
    try:
        next_link = soup.find(class_="next").find("a")["href"]
    except AttributeError:
        break
    next_page = short_url + str(next_link)
    response = requests.get(next_page)
    soup = BeautifulSoup(response.text, "html.parser")

print("""Welcome to the Guess That Quote Game!!!
You will have 4 tries to guess the author of a specific quote.  After every incorrect guess you
will receive a clue as to the authors identity.  Spelling, capitalization, and spelling matter.
""")
while True:
    while True:
        quote_item = random.choice(quote_list)
        quote, author, link = quote_item
        print(quote)
        user_answer = input("\nWho is the author of the above quote? ")
        if user_answer == author:
            print("Congratulations.  You are one smart cookie!")
            break
        response = requests.get(short_url + link)
        soup = BeautifulSoup(response.text, "html.parser")
        date = soup.find(class_="author-born-date").get_text()
        location = soup.find(class_="author-born-location").get_text()
        print("Hint 1: The author was born " + location + " on " + date)
        user_answer = input("What is your second guess? ")
        if user_answer == author:
            print("Congratulations.  You are smarter than the average bear!")
            break
        print("Hint 2: The author's first name begins with " + author[0].upper())
        user_answer = input("What is your third guess? ")
        if user_answer == author:
            print("Congratulations.  You are a champ!")
            break
        name_split = author.split(" ")
        print("Final Hint: The author's last name is " + name_split[len(name_split) - 1])
        user_answer = input("What is your final guess? ")
        if user_answer == author:
            print("Congratulations.  You beat the odds!")
            break
        print("I'm sorry.  The author's name was " + author + ".")
        break

    answer = input("\nWould you like to try again? (Y/N) ")
    if answer.upper() != "Y":
        break
    print()
