from bs4 import BeautifulSoup

with open('home.html','r') as page:
    content = page.read()
    soup = BeautifulSoup(content,'lxml')
    
    # To beautify the html code
    # print(soup.prettify())

    #to find single tag
    tag = soup.find('h5')
    
    #to find all tags
    tags = soup.find_all('h5')

    # to extract text from tags
    for content in tags:
        print(content.text)
    
    # searching with classes
    divs = soup.find_all('div', class_='some class')
    for div in divs:
        header = div.h2.text
        content = div.p.text
        next_page = div.a.text
    pass




# Scraping a real website
