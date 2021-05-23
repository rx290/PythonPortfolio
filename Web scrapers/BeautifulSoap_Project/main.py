from bs4 import BeautifulSoup
from bs4.builder import HTML
import requests


# to fetch the webpage

page = requests.get('')
soup = BeautifulSoup(page,'lxml')

