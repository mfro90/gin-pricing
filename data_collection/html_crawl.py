#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup

def extract_price_tags():
    tags = []
    for x in range(1, 100):
        # specify the url
        quote_str = "https://www.hjhansen-vin.dk/gin.aspx?pageIndex="
        quote_page = str(x)
        quote_page = quote_str + quote_page
    
    # query the website and return the html to the variable ‘page’
        try:
            page = urlopen(quote_page)
            response = page.getcode()
        except HTTPError:
            print("A total of " + len_list + " price tags have been extracted from " + quote_str)
            break
    
    # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page, "html.parser")

    # find all priceStor elements and store in BS4 obj 
        price_tags = soup.find_all("a", class_='priceStor')

    # parse items in list obj
        for t in price_tags:
            tags.append(t.string)
        len_list = str(len(tags))

    return tags
