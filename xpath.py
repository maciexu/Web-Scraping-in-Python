""" 
"/html/body/*" selects all elements one generation below the body element without concern of the tag type, i
t selects all children of the body element. 

On the other hand, "/html/body//*" selects all elements from all future generations of the body element 
(that is, all descendants of the body) regardless of tag type.

@ attribute
"""

# EXample 1
"""
<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello World!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose DataCamp!</p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Thanks for Watching!</p>
    </div>
  </body>
</html>
We have created the function print_element_text() for you, which will print any text contained in your element.

Tasks:
#1 Fill in the blanks in the XPath string to select the paragraph element containing the phrase: "Thanks for Watching!".
#2 Fill in the blanks in the xpath below to select the paragraph element containing the phrase: "Hello World!".
"""
# Create an Xpath string to select desired p element
xpath = '//*[@id="div3"]/p'

# Print out selection text
print_element_text( xpath )

# Create an XPath string to select p element by class
xpath = '//p[@class="class-1 class-2"]'

# Print out select text
print_element_text( xpath )

"""
<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello World!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose 
            <a href="http://datacamp.com">DataCamp!</a>!
        </p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Thanks for Watching!</p>
    </div>
  </body>
</html>

Tasks: 
1. Fill in the blanks to complete the variable xpath below to select the href attribute value from the DataCamp hyperlink.
"""

# Create an xpath to the href attribute
xpath = '//p[@id="p2"]/a/@href'

# Print out the selection(s); there should be only one
print_attribute( xpath )

"""Task 2 Fill in the blanks below to assign an XPath string to the variable xpath which directs to all href attribute values of 
the hyperlink a elements whose class attributes contain the string "course-block". 
Remember that we use the contains call within the XPath string to check if an attribute value contains a particular string.
"""
# Create an xpath to the href attributes
xpath = '//a[contains(@class,"course-block")]/@href'

# Print out how many elements are selected
how_many_elements( xpath )
# Preview the selected elements
preview( xpath )




