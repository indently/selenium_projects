from selenium import webdriver

# You need to add your own path to the webdriver here
chrome_driver = '/Users/macbook/Desktop/drivers/chromedriver'

# Here we instantiate the webdriver, so that we can use it for the project.
driver = webdriver.Chrome(chrome_driver)
driver.get('https://www.google.com')
