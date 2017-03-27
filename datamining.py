from selenium import webdriver
import time, os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
"""This script should take inputs as the color and size of a desired brick,
search the Lego 'Pick-a-Brick' website, and return the URL's for every brick"""

class Search(object):

    def __init__(self):
        # open up Google Chrome webpage
        self.driver = webdriver.Chrome('/home/kerry/chromedriver')

    def open_website(self):
        self.open_page = self.driver.get('http://www.shop.lego.com/pab/xhtml')
        self.view = time.sleep(3)
        self.driver.close()


"""driver = webdriver.Chrome('/home/kerry/chromedriver')
driver.get('http://www.google.com/xhtml')
assert 'Google' in self.driver.title
# elem.clear()
# elem.send_keys(Keys.RETURN)
time.sleep(3)
search = driver.find_element_by_name('q')"""

if __name__ == '__main__':
    search = Search()
    webpage = search.open_website()
    # main_function = search.main()

colors = ['black', 'blue', 'bright orange', 'brown', 'dark green', 'grey', 'lilac'
          'purple', 'red', 'reddish brown', 'silver', 'warm gold', 'white', 'yellow']
