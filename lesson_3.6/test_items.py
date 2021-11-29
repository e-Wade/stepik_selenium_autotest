import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_availability(browser):
    browser.get(link)
    time.sleep(30)
    add_to_cart_button = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(add_to_cart_button) == 1, 'the button is not available or unique'
    