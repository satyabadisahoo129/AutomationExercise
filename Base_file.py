import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re



class Login:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
    login_tab=(By.XPATH,"//ul[@class='nav navbar-nav']//li[4]")
    user_name=(By.XPATH,"//input[@data-qa='login-email']")
    password=(By.XPATH,"//input[@name='password']")
    login_button=(By.XPATH,"//button[@data-qa='login-button']")
    logout=(By.XPATH,"//a[@href='/logout']")
    def go_for_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_tab)).click()
    def do_login(self,email,pswd):
        self.wait.until(EC.presence_of_element_located(self.user_name)).send_keys(email)
        self.wait.until(EC.presence_of_element_located(self.password)).send_keys(pswd)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        logout_button=self.wait.until(EC.presence_of_element_located(self.logout))
        assert logout_button.is_displayed(), 'Something went wrong'
    def do_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.logout)).click()

class Product:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
    product_button=(By.XPATH,"//a[@href='/products']")
    search_bar=(By.XPATH,"//input[@name='search']")
    search_button=(By.XPATH,"//button[@id='submit_search']")
    product_item =(By.XPATH,"//a[@href='/product_details/2']")
    price_tag=(By.XPATH,"//div[@class='col-sm-7']//span/span")
    qty_bar=(By.XPATH,"//input[@id='quantity']")
    add_cart_button=(By.XPATH,"//button[@class='btn btn-default cart']")
    continue_shop=(By.XPATH,"//button[@class='btn btn-success close-modal btn-block']")
    cart_button=(By.XPATH,"//a[@href='/view_cart']")
    check_out=(By.XPATH,"//a[@class='btn btn-default check_out']")
    place_order=(By.XPATH,"//a[@class='btn btn-default check_out']")
    card_name=(By.XPATH,"//input[@class='form-control']")
    card_number=(By.XPATH,"//input[@data-qa='card-number']")
    cvv=(By.XPATH,"//input[@data-qa='cvc']")
    exp_month=(By.XPATH,"//input[@data-qa='expiry-month']")
    exp_year=(By.XPATH,"//input[@data-qa='expiry-year']")
    payment=(By.XPATH,"//button[@data-qa='pay-button']")
    confirmation_message=(By.XPATH,"//div[@class='col-sm-9 col-sm-offset-1']//p")


    def click_product(self):
        self.wait.until(EC.element_to_be_clickable(self.product_button)).click()
    def do_search(self,item):
        self.wait.until(EC.presence_of_element_located(self.search_bar)).send_keys(item)
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()
    def view_product(self,product_no):
        xpath=f"//a[@href='/product_details/{product_no}']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH,xpath))).click()
        # items_price=self.wait.until(EC.presence_of_element_located(self.price_tag))
        # rate_per=items_price.text
        # match=re.search(r'\d+',rate_per)
        # return float(match.group())
    # def qty_order(self,qty):
    #     quantity=self.wait.until(EC.presence_of_element_located(self.qty_bar))
    #     quantity.clear()
    #     quantity.send_keys(qty)
        # final_price=self.view_product()*qty
        # print('Total price : ',final_price)
        # time.sleep(4)
        # return final_price
    def add_to_cart(self):
        cart=self.wait.until(EC.element_to_be_clickable(self.add_cart_button))
        self.driver.execute_script('arguments[0].click()',cart)
        self.wait.until(EC.element_to_be_clickable(self.continue_shop)).click()
    def click_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_button)).click()
    def check_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.cart_button)).click()
        try:
            table=self.wait.until(EC.presence_of_element_located((By.XPATH,"//table")))
            if table.is_displayed():
                print('product avialable')
        except:
            print('Product not in the cart')
    def cart_qty_update(self,qty,product_no):
        xpath = f"//a[@href='/product_details/{product_no}']"
        # self.wait.until(EC.element_to_be_clickable(self.cart_button)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH,xpath))).click()
        quantity = self.wait.until(EC.presence_of_element_located(self.qty_bar))
        quantity.clear()
        quantity.send_keys(qty)
        self.click_cart()
        # self.wait.until(EC.element_to_be_clickable(self.add_cart_button)).click()

    def cart_delete(self,product_id):
        try:
            if product_id:
                product_id=str(product_id)
                xpath=f"//a[@data-product-id='{product_id}']"
                self.driver.find_element(By.XPATH,xpath).click()
                print('item succesfully deleted from cart')
            else:
                print('item not found')
        except:
            print('No product is cart to delete')
    def cart_amount_check(self):
        self.click_cart()
        self.wait.until(EC.element_to_be_clickable(self.check_out)).click()
        total_calculated=0
        for i in range(1,3):
            price=self.wait.until(EC.presence_of_element_located((By.XPATH,f"//table[@class='table table-condensed']//tbody/tr[{i}]/td[3]")))
            qty=self.wait.until(EC.presence_of_element_located((By.XPATH,f"//table[@class='table table-condensed']//tbody/tr[{i}]/td[4]")))
            act_price=int(re.sub(r'[^\d]','',price.text))
            act_qty=int(re.sub(r'[^\d]','',qty.text))
            total_calculated=total_calculated+(act_qty*act_price)
        cart_price=self.wait.until(EC.presence_of_element_located((By.XPATH,"//table[@class='table table-condensed']//tbody/tr[2]/td[4]")))
        act_cart_price=int(re.sub(r'[^\d]','',cart_price.text))
        if total_calculated==act_cart_price:
            return True
        else:
            return False
    def Place_Order(self):
        if self.cart_amount_check():
            placeOrder=self.wait.until(EC.element_to_be_clickable(self.place_order))
            self.driver.execute_script('arguments[0].click()',placeOrder)
        else:
            print('price not matching')
    def payment_confirmation(self):
        self.wait.until(EC.presence_of_element_located(self.card_name)).send_keys('Satya')
        self.wait.until(EC.presence_of_element_located(self.card_number)).send_keys('1234567891234')
        self.wait.until(EC.presence_of_element_located(self.cvv)).send_keys('345')
        self.wait.until(EC.presence_of_element_located(self.exp_month)).send_keys('04')
        self.wait.until(EC.presence_of_element_located(self.exp_year)).send_keys('1987')
        self.wait.until(EC.element_to_be_clickable(self.payment)).click()
        message=self.wait.until(EC.presence_of_element_located(self.confirmation_message))
        assert 'Congratulations' in message.text, "Order Not placed"
























