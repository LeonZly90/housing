# https://www.browserstack.com/guide/run-selenium-tests-using-selenium-chromedriver
# https://pythonhowtoprogram.com/how-to-scrape-javascript-websites-with-selenium-using-python-3/
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchWindowException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# chrome_options = Options()
# chrome_options.add_argument('--headless')

# this constant should be modified according to where the web driver has been placed
WEBDRIVER_PATH = r'C:\Users\LZhang\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(WEBDRIVER_PATH)
# driver = webdriver.Chrome(ChromeDriverManager().install())

# define URL
# URL = 'https://www.google.com'
URL = 'https://www.noradarealestate.com/real-estate-investments/'

driver.get(URL)
print(driver.title)
# search_box = driver.find_element_by_xpath('//input[@id="search"]')
# search_box.send_keys('Selenium')
# search_box.send_keys(Keys.ENTER)

driver.implicitly_wait(10)
input1 = driver.find_element_by_link_text('2')
input2 = driver.find_element_by_link_text('3')
# input3 = driver.find_element_by_link_text('4')
actions = ActionChains(driver)
actions.move_to_element(input1)
actions.click(input1)
# time.sleep(5)
actions.move_to_element(input2)
actions.click(input2)

actions.perform()

