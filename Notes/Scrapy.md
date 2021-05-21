# Introduction

    Scrapy is a free open source web-crawling framework written in python, it is used to extract data using both APIs and and general purpose web crawler.

## Explanation

    Scrapy has builtin mechanism for extracting data called selectors either you can use html selector or RE selectors to fetch all the data.

    response.css("attribute")

## Working

    To get started with scrapy we just need to setup a virtual environment and install scrapy to it with command:
    
    pip install scrapy
    
    activate the environment and create a Scrapy project with the command

    scrapy createproject "Project Name without quotes"

    A scrapy project will be created after that shift to the project directory by cd command and then generate a basic spider by the command

    scrapy genspider "Name" "URL to Scrape"

    To utilize scrapy completely one must master its shell to extract a sample of data, i.e. to prepare data models in items.py for scrapy to scrape data accordingly to open shell one must open CLI and type in following command

    scrapy shell

### Basic Shell Commands

    1. response.css('title').get(): 
            what this command is doing is fetching "<title> </title>" element in the HTML webpage.

    2. ::text 
        This is a sub addition to the above command to fetch child text encapsulated inside the html elements. 
        response.css('title').get() 
        This will fetch <title> some title </title> 
        but by using response.css('title::text').get() 
        we will only fetch "some title"

    3. let say we have multiple we have multiple html elements like headings, spans, div or paragraphs so what we could do is 
        we can use indexing to fetch them with the above command for example: 
        response.css('h2::text')[1].get() 
        That command is going to fetch the second h2 heading text from the webpage. 
        note: index always starts with 0 until overridden

    4. How can we get all elements of the same type? 
        That is pretty simple just type the above mentioned command without indexer and use getall instead of get i.e. 
        response.css('h2::text').getall()

    5. Selecting by class and id: 
        "." is the notation used for class in css and "#" is the notation used for id. Same things are applicable in scrapy for eg: 
        response.css('.chr-a').getall() 
        it will fetch every element with the class name let say we only need to find anchors with that class then we could do this: 
        response.css('.chr-a a').getall() 
        if we only need all text from anchors then we will do this: 
        response.css('.chr-a a::text').getall()

    6. Selecting by using regular expression 
        we have a property known as re which is used to fetch data with regular expressions for example: 
        response.css('P::text').re(r 'rimuru')

        rimuru is the name of a character in a light novel and i just want to fetch the word rimuru from all paragraphs

    7. we can also use xpath to fetch data which is as follows 
        response.xpath('//h3') to get all h3 
        to extract the encapsulated child we are required to use /text and extract() property for eg: 
        response.xpath('//h3/text').extract() or response.xpath('//h3/text').getall()

scrapy crawl "Crawler Name without quotes"

## Settings

## Example
