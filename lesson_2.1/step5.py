from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
  
link = "http://suninjuly.github.io/math.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    time.sleep(0.5)
    
    browser.find_element_by_id('robotCheckbox').click()
    time.sleep(0.5)
    browser.find_element_by_id('robotsRule').click()
    time.sleep(0.5)
    
    browser.find_element_by_css_selector("button[type='submit']").click()
    
    alert = browser.switch_to_alert()
    print(alert.text)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
