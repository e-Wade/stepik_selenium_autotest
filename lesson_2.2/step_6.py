from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    
    
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id('input_value').text
    result = calc(x)
    
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(result)
    time.sleep(0.5)
    
    browser.execute_script("return arguments[0].scrollIntoView();", answer_field)
    time.sleep(0.5)
    
    browser.find_element_by_id('robotCheckbox').click()
    time.sleep(0.5)
    browser.find_element_by_id('robotsRule').click()
    time.sleep(0.5)
        
    browser.find_element_by_css_selector("button[type='submit']").click()
    
    alert = browser.switch_to_alert()
    print(alert.text)
    
    
finally:
    time.sleep(10)
    #browser.quit()
    browser.quit()