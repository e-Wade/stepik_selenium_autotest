from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    
    
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element_by_class_name('btn-primary').click()
    browser.switch_to.alert.accept()
    time.sleep(1)
    
    x = browser.find_element_by_id('input_value').text
    result = calc(x)
    
    answer_field = browser.find_element_by_id('answer')
    answer_field.send_keys(result)
    time.sleep(0.5)

    browser.find_element_by_css_selector("button[type='submit']").click()
    
    alert = browser.switch_to.alert
    print(alert.text)
    
    
finally:
    time.sleep(10)
    #browser.quit()
    browser.quit()