# From Tree to HTML
html = '''
<html>
  <head>
    <title>Intro HTML</title>
  </head>
  <body>
    <p>Hello World!</p>
    <p>Enjoy DataCamp!</p>
  </body>
</html>
'''


""" Example 1
Consider the HTML code:

<html>
  <body>
    <div>
      <p>Good Luck!</p>
      <p>Not here...</p>
    </div>
    <div>
      <p>Where am I?</p>
    </div>
  </body>
</html>
Your job will be to create an XPath string using single forward-slashes and brackets which navigates to the paragraph p element 
which contains the text "Where am I?".

Note: Using only single forward-slashes to move between generations, and brackets to select the correct element.
"""

xpath = '/html/body/div[2]/p[1]'


""" double forward-slashes to navigate to all future generations. """

""" we can do is select elements by their attributes using an XPath. 
For example, if we want to direct to the div element within the HTML document whose id attribute is "uid", 
then we could write the XPath string '//div[@id="uid"]'. 
The first part of this string, //div, first looks at all div elements in the HTML document. 
Then, using the brackets, we specify that we want only the div element with a specific id attribute (in this case uid). 
To note, the phrase @id="uid" in the brackets would be read as "attribute id equals uid".
"""
# Example 2 -->> 
# Assign to the variable xpath an XPath string which will select all span elements whose class attribute equals "span-class". 

xpath = '//span[@class="span-class"]'
