""" The (X)Path to CSS Locators """

# Create the XPath string equivalent to the CSS Locator 
xpath = '/html/body/span[1]//a'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'html > body > span:nth-of-type(1) a'

# Create the XPath string equivalent to the CSS Locator 
xpath = '//div[@id="uid"]/span//h4'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'div#uid > span h4'

""" Hint
Remember to use a period . when trying to select by class.
Remember to use the greater than > symbol when moving down a generation.

 Select the hyperlink (a element) children of all div elements belonging to the class "course-block" 
 (that is, any div element with a class attribute such that "course-block" is one of the classes assigned). 
 The number of such elements is 11, so you can check your solution with how_many_elements if you choose.
"""

from scrapy import Selector
css_locator = 'div.course-block > a'

# Print the number of selected elements.
how_many_elements( css_locator )


""" The CSS Wildcard
In fact, we can use it in a similar way, when we want to ignore the tag type. For example:

The CSS Locator string '*' selects all elements in the HTML document.

The CSS Locator string '*.class-1' selects all elements which belong to class-1, 
but this is unnecessary since the string '.class-1' will also do the same job.

The CSS Locator string '*#uid' selects the element with id attribute equal to uid, 
but this is unnecessary since the string '#uid' will also do the same job.
"""
# Create the CSS Locator to all children of the element whose id is uid
css_locator = '#uid>*'




""" CSS Attributes and Text Selection 
In a previous exercise, you created a CSS Locator string to select the hyperlink (a element) children of 
all div elements belonging to the class "course-block". 
Here we have created a SelectorList called course_as having selected those hyperlink children.

Now, we want you to fill in the blank below to extract the href attribute values from these elements. 
This is another example of chaining, as we've seen in a previous exercise.

The point here is that we can chain together calls to the methods css and xpath, and combine them! 
We help nudge you in the correct direction by giving you the solution if we chain with another call to the css method.
"""
from scrapy import Selector

# Create a selector object from a secret website
sel = Selector( text = html )

# Select all hyperlinks of div elements belonging to class "course-block"
course_as = sel.css( 'div.course-block > a' )

# Selecting all href attributes chaining with css
hrefs_from_css = course_as.css( '::attr(href)' )

# Selecting all href attributes chaining with xpath
hrefs_from_xpath = course_as.xpath( './@href' )


"""Example 1:  Assign to the variable xpath an XPath string directing to the text within the paragraph p element with id equal to p3, 
which does NOT include the text of future generations of this p element.
"""
xpath = '//p[@id="p3"]/text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3::text'

# Print the text from our selections
print_results( xpath, css_locator )


"" Example 2: Assign to the variable xpath an XPath string directing to the text within the paragraph p element with id equal to p3, 
which includes the text of future generations of this p element.
"""
# Create an XPath string to the desired text. Compare with Example1, it is  //. 
xpath = '//p[@id="p3"]//text()'

# Create a CSS Locator string to the desired text. Compare with Example1, there's a space before ::
css_locator = 'p#p3 ::text'

# Print the text from our selections
print_results( xpath, css_locator )

