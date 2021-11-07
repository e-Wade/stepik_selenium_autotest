from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
    
    
link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена дома не станет равно 100
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element_by_id('book').click()
    
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