""" XPath Chaining
Selector and SelectorList objects allow for chaining when using the xpath method. 
What this means is that you can apply the xpath method over once you've already applied it. 
For example, if sel is the name of our Selector, then

sel.xpath('/html/body/div[2]')
is the same as

sel.xpath('/html').xpath('./body/div[2]')
or is the same as

sel.xpath('/html').xpath('./body').xpath('./div[2]')
"""
from scrapy import Selector

# Create a Selector selecting html as the HTML document
sel = Selector( text = html )

# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath( '//div' )


# Requesting a Selector
# Import a scrapy Selector
from scrapy import Selector

# Import requests
import requests

# Create the string html containing the HTML source
html = requests.get( url ).content

# Create the Selector object sel from html
sel = Selector( text = html )

# Print out the number of elements in the HTML document
print( "There are 1020 elements in the HTML document.")
print( "You have found: ", len( sel.xpath('//*') ) )   # 1020


