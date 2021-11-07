from selenium import webdriver
import os
import time


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_css_selector('[name=firstname]')
    input1.send_keys('Vadim')
    time.sleep(0.5)
    
    input2 = browser.find_element_by_css_selector('[name=lastname]')
    input2.send_keys('Gener')
    time.sleep(0.5)
    
    input3 = browser.find_element_by_name('email')
    input3.send_keys('Gener@mail.com')
    time.sleep(0.5)
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    choose_file_but = browser.find_element_by_id('file')
    choose_file_but.send_keys(file_path)
    time.sleep(0.5)
    
    browser.find_element_by_css_selector('[type=submit]').click()
    
    
    alert = browser.switch_to_alert()
    print(alert.text)
    
    
finally:
    time.sleep(10)
    #browser.quit()
    browser.quit()