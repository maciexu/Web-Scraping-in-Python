# use a pre-loaded Response object, named response to scrape the course titles from the (shortened version of the) DataCamp course directory 
# https://www.datacamp.com/courses/all.

# Create a SelectorList of the course titles
crs_title_els = response.css( 'h4::text' )

# Extract the course titles 
crs_titles = crs_title_els.extract()

# Print out the course titles 
for el in crs_titles:
  print( ">>", el )


""" Scraping with Children
To be explicit, we have created the Selector object mystery in the following way:

We first loaded a Response variable using a secret website as the input.
Then we used a call to the xpath method to create a SelectorList of elements (but we won't say which ones)
Finally, we let mystery be the first Selector object of this SelectorList.
"""
# Calculate the number of children of the mystery element
how_many_kids = len( mystery.xpath( './*' ) )

# Print out the number
print( "The number of elements you selected was:", how_many_kids )



