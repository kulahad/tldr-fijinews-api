from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
# option.add_argument("--headless")

# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path=r'D:/Projects/Python 3/chromedriver', chrome_options=option)

# Go to desired website
browser.get("https://fijivillage.com/")
# Wait 20 seconds for page to load
timeout = 20
try:
    # Wait until the final element [Logo] is loaded.
    # Assumption: If Logo is loaded, the whole page would be relatively loaded because it is among
    # the last things to be loaded.
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Fijivillage']")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()

# Get all of the titles for the pinned repositories
# We are not just getting pure titles but we are getting a selenium object
# with selenium elements of the titles.

# find_elements_by_xpath - Returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath("//div[@class='col-md-3 pt-2']")

# List Comprehension to get the actual titles and not the selenium objects.
titles = [x.text for x in titles_element]

# print response in terminal
print('TITLES:')
print(titles_element, '\n')

print('EACH TITLES:')
for val in titles_element:
    try:
        val
    except NameError:
        print("well, it WASN'T defined after all!")
    else:
        print("sure, it was defined.")
        print(val.text)


browser.quit()
