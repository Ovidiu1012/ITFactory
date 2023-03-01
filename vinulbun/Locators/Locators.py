from selenium.webdriver.common.by import By
from Utils.Variables import Variables

class HomepageLocators:
    URL="https://vinulbun.ro/"
    age_verify = (By.ID, 'age-verify')
    age_verify_true = (By.XPATH,'//*[@id="age-verify"]/div/button')
    search = (By.ID, 'cauta')
    search_button = (By.XPATH,'//*[@id="header"]/div/div[2]/div/div[2]/div/form/div/button/i')
    home_button = (By.ID, 'header')
    login = (By.XPATH, '//*[@id="header"]/div/div[1]/div/div[3]/a')

class SearchpageLocators:
    URL="https://vinulbun.ro/caut?TextDeCautat=" + Variables.search_item + "&ClasaCautare=0"
    item_results = (By.PARTIAL_LINK_TEXT, Variables.search_item)
    add_to_cart_button = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/div/div/ul/li/div/div/div[6]/a[2]')
    notification_add = (By.CLASS_NAME, 'notification ui-pnotify-container notification-success')
    cart = (By.XPATH,'//*[@id="cart-navbar"]/a')

class ItempageLocators:
    add_to_cart_button = (By.XPATH, '//*[@id="chart_div"]/button')
    notification_add = (By.CLASS_NAME, 'ui-pnotify')
    cart_qty = (By.CLASS_NAME,'cart-qty')


class CartpageLocators:
    empty_cart = (By.XPATH, '//*[@id="produse_in_cos"]/div/table/tfoot/tr[3]/td/button[1]')
    confirm_empty = (By.XPATH, '//*[@id="btn-confirm-modal"]')
    warning = (By.CLASS_NAME, 'text-danger')
    order = (By.XPATH, '//*[@id="produse_in_cos"]/div/table/tfoot/tr[3]/td/button[2]')
    cookies = (By.XPATH,'html/body/div[1]/div[5]/div/div/div[2]/a')

class LoginpageLocators:
    URL="https://vinulbun.ro/login"
    user = (By.ID, 'email_login')
    password = (By.NAME, 'password')
    login_btn = (By.XPATH, '//*[@id="FormAutentificare"]/div[3]/input')

class SecurepageLocators:
    URL="https://vinulbun.ro/contul-meu"
    verify = (By.XPATH,'//*[@id="parola_cont"]/div/div/div[1]/div/h2/strong')
    verify2 = (By.ID,'modific_cont_nume')

class OrderpageLocators:
    delivery_mode = (By.XPATH, '//*[@id="FormAdaugConanda"]/div[7]/div[2]/label/span')
    payment_mode = (By.XPATH, '//*[@id="FormAdaugConanda"]/div[10]/div[2]/label/span')
    details = (By.ID, 'obs_comanda')
    terms = (By.XPATH, '//*[@id="FormAdaugConanda"]/div[11]')
    notify_delivery = (By.CLASS_NAME, 'ui-pnotify-text')
    notify_payment = (By.CLASS_NAME, 'ui-pnotify-text')
    place_order = (By.XPATH, '//*[@id="FormAdaugConanda"]/div[12]/div/button')