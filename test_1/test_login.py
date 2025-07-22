import time

import pytest
from Base_file import Login,Product

@pytest.mark.parametrize('email,pswd',[('satyabadisahoo0@gmail.com','Satyabadi@1987'),('pela@nerolac.com','banda')])
def test_login_credential(driver,email,pswd):
    logging=Login(driver)
    logging.go_for_login()
    logging.do_login(email,pswd)

def test_logout(driver):
    logging_obj=Login(driver)
    logging_obj.go_for_login()
    logging_obj.do_login('satyabadisahoo0@gmail.com','Satyabadi@1987')
    logging_obj.do_logout()
    assert '/login' in driver.current_url

def test_tillcart(driver):
    loggin=Login(driver)
    loggin.go_for_login()
    loggin.do_login('satyabadisahoo0@gmail.com','Satyabadi@1987')
    product=Product(driver)
    product.click_product()
    product.do_search('Tshirt')
    product.view_product()
    product.qty_order(2)
    product.add_to_cart()

def test_check_cart(driver):
    loggin = Login(driver)
    loggin.go_for_login()
    loggin.do_login('satyabadisahoo0@gmail.com', 'Satyabadi@1987')
    product = Product(driver)
    product.click_product()
    product.do_search('Tshirt')
    product.view_product()
    product.qty_order(2)
    product.add_to_cart()
    product.check_cart()

def test_cart_quantity_update(driver):
    loggin = Login(driver)
    loggin.go_for_login()
    loggin.do_login('satyabadisahoo0@gmail.com', 'Satyabadi@1987')
    product = Product(driver)
    product.click_product()
    product.do_search('Tshirt')
    product.view_product(28)
    product.add_to_cart()
    product.cart_qty_update(3,28)

def test_remove_qty(driver):
    loggin = Login(driver)
    loggin.go_for_login()
    loggin.do_login('satyabadisahoo0@gmail.com', 'Satyabadi@1987')
    product = Product(driver)
    product.click_cart()
    time.sleep(2)
    product.cart_delete(2)


def test_check_out(driver):
    loggin = Login(driver)
    loggin.go_for_login()
    loggin.do_login('satyabadisahoo0@gmail.com', 'Satyabadi@1987')
    product = Product(driver)
    product.click_product()
    product.do_search('Tshirt')
    product.view_product(28)
    product.add_to_cart()
    product.cart_qty_update(2,28)
    # product.cart_amount_check()
    product.Place_Order()
    product.payment_confirmation()










