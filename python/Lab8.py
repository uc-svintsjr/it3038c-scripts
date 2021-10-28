#Name: Joseph Svintsitsky
#Module: Lab 8
#Due Date: 10/31/2021
#Assignment: Using a website of your choice, extract some valuable data from it and print it to the console.
#Resources: https://code.datasciencedojo.com/datasciencedojo/tutorials/blob/master/Web%20Scraping%20with%20Python%20and%20BeautifulSoup/Web%20Scraping%20with%20Python%20and%20Beautiful%20Soup.py
#URL: https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card

import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# URl to web scrap from.
newegg_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# Opens URL and grabs data from the web page.
openURL = urlopen(newegg_url)
webHTML = openURL.read()
openURL.close()

# HTML parsing in a soup data structure.
parseSoup = soup(webHTML, 'html.parser')

# Grabbing all containers with class name = item-container
containers = parseSoup.findAll('div', {'class':'item-container'})

# Output csv file to write to local disk.
filename = "GPUs.csv"
f = open(filename, 'w')

# Writes headers for the csv file.
headers = "Brands, Product Name, Shipping\n"
f.write(headers)

# Each product has its own row in the csv file.
container = containers[1]

# Loops over each product and grabs attributes about each product brand, Product Name, and Shipping.
for container in containers:
    brand = container.div.div.a.img['title']
    title_container = container.findAll('a', {'class':'item-title'})
    product_name = title_container[0].text
    ship_container = container.findAll('li', {'class':'price-ship'})

    # Use strip() to remove blank spaces before and after text.
    shipping = ship_container[0].text.strip()

    # Prints out the results in the console.
    print("Brand:" + brand)
    print("Product Name:" + product_name)
    print("Shipping:" + shipping)

    # Writes the dataset to the csv file.
    f.write(brand + ',' + product_name.replace(',' , '|') + ',' + shipping + '\n')

# Close the file.
f.close()
