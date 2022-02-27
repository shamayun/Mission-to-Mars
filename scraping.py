
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# set up the URL (NASA Mars News (Links to an external site.)) for scraping.
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1) #optional delay is useful, dynamic pages take longer to load

# I've assigned slide_elem as the variable to look for the <div /> tag and its descendent (the other tags within the <div /> element). This is parent element. This means that this element holds all of the other elements within it, and I'll reference it when we want to filter search results even further. The (.) is used for selecting classes, such as list_text, so the code 'div.list_text' pinpoints the <div /> tag with the class of list_text. CSS works from right to left, such as returning the last item on the list instead of the first. Because of this, when using select_one, the first matching element returned will be a <li /> element with a class of slide and all nested elements within it.

#set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

#This variable holds a ton of information, so look inside of that information to find this specific data.
slide_elem.find('div', class_='content_title') #The specific data is in a <div /> with a class of 'content_title'."

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text() # get_text(), only the text of the element is returned
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1] # browser to click the second button
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='headerimage fade-in').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# scrape the entire table with Pandas' .read_html() function
df = pd.read_html('https://galaxyfacts-mars.com')[0] # index of 0, telling Pandas to pull only the first table/first item in list
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# convert our DataFrame back into HTML-ready code
df.to_html() # it's a <table /> element with a lot of nested elements

# turning off the browser
browser.quit()


