from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    
    result = int(num1) + int(num2)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))
    time.sleep(1)
    
    browser.find_element_by_css_selector("button[type='submit']").click()
    
    alert = browser.switch_to_alert()
    print(alert.text)
    
    
finally:
    time.sleep(10)
    #browser.quit()
    browser.quit()