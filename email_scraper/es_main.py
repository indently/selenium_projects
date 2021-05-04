import re
from selenium import webdriver

# You need to add your own path to the webdriver here
chrome_driver = '/Users/macbook/Desktop/drivers/chromedriver'

# Here we instantiate the webdriver, so that we can use it for the project.
driver = webdriver.Chrome(chrome_driver)
driver.get("https://www.randomlists.com/email-addresses?qty=100")

# Get the page source code
page_source = driver.page_source

# Regex to find e-mails
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# Create a list and add all the emails
list_of_emails = []

# Finds all the emails
for re_match in re.finditer(EMAIL_REGEX, page_source):
    list_of_emails.append(re_match.group())

# Lists all the e-mails that we managed to scrape
for i, email in enumerate(list_of_emails):
    print(f'{i + 1}: {email}')

# Close the driver since we don't need it
driver.close()
