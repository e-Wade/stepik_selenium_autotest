from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
  
link = "http://suninjuly.github.io/get_attribute.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    treasure_img = browser.find_element_by_id('treasure')
    x_element = treasure_img.get_attribute('valuex')
    y = calc(x_element)
    
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
