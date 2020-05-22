#  Example 1
# Import scrapy library
import scrapy

# Create the spider class
class YourSpider(scrapy.Spider):
  name = "your_spider"
  # start_requests method
  def start_requests(self):
    pass
  # parse method
  def parse(self, response):
    pass
  
# Inspect Your Class
inspect_class(YourSpider)



# Example 2
# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    urls = ["https://www.datacamp.com", "https://scrapy.org"]
    for url in urls:
      yield url
  # parse method
  def parse( self, response ):
    pass
  
# Inspect Your Class
inspect_class( YourSpider )


""" requests 
Self Referencing is Classy
You probably have noticed that within the spider class, we always input the argument self in the start_requests and parse methods 
(just look in the sample code in this exercise!). This allows us to reference between methods within the class. 
That is, if we want to refer to the method parse within the start_requests method, 
we would need to write self.parse rather than just parse; what writing self does is tell the code: 
"Look in the same class as start_requests for a method called parse to use."
"""
# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    self.print_msg( "Hello World!" )
  # parse method
  def parse( self, response ):
    pass
  # print_msg method
  def print_msg( self, msg ):
    print( "Calling start_requests in YourSpider prints out:", msg )
  
# Inspect Your Class
inspect_class( YourSpider )



""" use the yielded scrapy.Request to direct to the correct URL and parsing method """
# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url="https://www.datacamp.com", callback=self.parse )
  # parse method
  def parse( self, response ):
    pass
  
# Inspect Your Class
inspect_class( YourSpider )




""" Example: Within the parse method, create a variable author_names, 
which is a list of strings created by extracting the text from the paragraph elements belonging to the class course-block__author-name.
"""
# Import the scrapy library
import scrapy

# Create the Spider class
class DCspider( scrapy.Spider ):
  name = 'dcspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  # parse method
  def parse( self, response ):
    # Create an extracted list of course author names
    author_names = response.css( 'p.course-block__author-name::text' ).extract()
    # Here we will just return the list of Authors
    return author_names
  
# Inspect the spider
inspect_spider( DCspider )



""" Example: This will be your first chance to play with a spider which will crawl between sites 
(by first collecting links from one site, and following those links to parse new sites). 
This spider starts at the shortened DataCamp course directory, then extracts the links of the courses in the parse method; 
from there, it will follow those links to extract the course descriptions from each course page in the parse_descr method, 
"""
# Import the scrapy library
import scrapy

# Create the Spider class
class DCdescr( scrapy.Spider ):
  name = 'dcdescr'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  
  # First parse method
  def parse( self, response ):
    links = response.css( 'div.course-block > a::attr(href)' ).extract()
    # Follow each of the extracted links
    for link in links:
      yield response.follow(url = link, callback = self.parse_descr)
      
  # Second parsing method
  def parse_descr( self, response ):
    # Extract course description
    course_descr = response.css( 'p.course__description::text' ).extract_first()
    # For now, just yield the course description
    yield course_descr

# Inspect the spider
inspect_spider( DCdescr )


