from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get("http://bit.ly/2EN2Ntv").text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")
    # find the title
    title_list = soup.find(class_="dotd-title")
    title_list_items = title_list.find_all("h2")
    the_title = title_list_items[0].getText().strip()
    # find the description
    description_list = soup.find(class_="dotd-main-book-summary float-left")
    description_items = description_list.find_all("div")
    the_description = description_items[2].getText().strip()
    # find the image
    image_list = soup.find(class_="bookimage imagecache imagecache-dotd_main_image")
    the_image = image_list.get("src")
    # and finally, find the link
    link_list = soup.find(class_="dotd-main-book-image float-left")
    link_list_items = link_list.find_all("a")
    the_link = link_list_items[0].get("href")
    # put everything together
    book = Book(the_title, the_description, the_image, the_link)
    return book
