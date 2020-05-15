from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--headless")

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
Divs_element = browser.find_elements_by_xpath("//div[@class='row mt-2']")

# Find all h6 elements in parent div element

for Parent_Div in Divs_element:
    all_children_by_xpath = Parent_Div.find_elements_by_xpath(".//*")
    for child in all_children_by_xpath:
        # Check for 'h' elements and use it as 'Title'
        # Check for 'a' elements and use it as 'Link'
        # Check for 'span' elements and use it as 'NewsAge'
        # Check for 'inner div' elements and use it as 'Short Description'
        print("child : " + child.tag_name, child.text)
    print("Parent Div:")
    title = Parent_Div.find_element_by_css_selector('h6')

    try:
        title
    except NameError:
        print("well, it WASN'T defined after all!")
    else:
        print("Title: ", title.text)

    link_element = Parent_Div.find_element_by_css_selector('a')
    try:
        link_element
    except NameError:
        print("well, it WASN'T defined after all!")
    else:
        link = link_element.get_attribute("href")
        print("Link: ", link)
        print("\n")

# print('TITLES:')
# for title in Title_element:
#     for val in title:
#         print(val.text, '\n')
#
# print('LINKS:')
# for link in link_element:
#     for val in link:
#         print(val.text, '\n')
# # List Comprehension to get the actual titles and not the selenium objects.
# Divs = [x.text for x in Divs_element]
#
# # print response in terminal
# print('Divs:')
# print(Divs_element, '\n')

# print('EACH TITLES:')
# for val in Divs_element:
#     try:
#         val
#     except NameError:
#         print("well, it WASN'T defined after all!")
#     else:
#         print("sure, it was defined.")
#         print(val.text)


browser.quit()
