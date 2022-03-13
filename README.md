# Mission-to-Mars
## Overview:
 Automation of Web scraping to extract data, web page constuction using HTML, CSS. Automating web browsers with Splinter, Beautiful Soup. Store data in MongoDB. Finally utilize Flask to update page with newest data.
## Resources
* Python 
* Flask
* JupyterLab
* VS Code 
* MongoDB
* HTML 
* Bootstrap 3
## Scraping to Final Output
**Web Scraping:** A python script (scarpping.py) containing required parameters and code to perform specified web scraping to collect and format data (raw text strings, image urls, etc).

**MongoDB:** The non-relational database is used to store the scraped data within a BSON(Binary encoding of JSON) format.This is necessary since there is no specific or orderly structure to retrieval of data.

**Flask App:** Another separate python script (app.py) is used to define the framework. This allows communication between the scraping script and the NoSQL database, as well as the html components needed to display the webpage in local server.

**HTML:** To display the data in a specific format, html and CSS layout built to parameters which allows the Flask App to pass through data.

## Results:
Once all the above stpes were followed, I was able to get the following output.
![](/Resources/mission_to_mars_scrapping.png "Final Result from Scarpping Data")
