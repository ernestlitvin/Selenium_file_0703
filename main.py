import time

from selenium.webdriver.common.by import By
from selenium import webdriver

## UZD 1 ##

'''
sukurti vartotoją
įkelti skelbimą užpildant visus laukus (ir įkeliant nuotrauką. įsitikinkite, 
ar nuotrauka tikrai įsikėlė) patestuokite kaip veikia keliant kelias nuotraukas.
'''

'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://elenta.lt/")

driver.find_element(By.CLASS_NAME,"fc-cta-consent").click()
driver.get("https://elenta.lt/registracija")

driver.find_element(By.ID,'UserName').send_keys("sveikiLABA123")
driver.find_element(By.ID,'Email').send_keys("manopastas@pastas.lt")
driver.find_element(By.ID,'Password').send_keys("Manopsw123")
driver.find_element(By.ID,'Password2').send_keys("Manopsw123")
driver.find_element(By.CLASS_NAME,'bigNavBtn2').click()
time.sleep(1)

driver.find_element(By.ID,'submit-new-ad-nav-button').click()

# driver.find_element(By.ID,"search-page-box").send_keys("automobilis")
# driver.find_element(By.CLASS_NAME,"search-button").click()
# driver.find_element(By.TAG_NAME,"Prisijungti prie eLenta.lt").click()

driver.get("https://elenta.lt/patalpinti/pasirinkti-kategorija/automoto?returnurl=%2Fpatalpinti%2Fpasirinkti-kategorija")
driver.get("https://elenta.lt/patalpinti/ivesti-informacija?categoryId=AutoMoto_Automobiliai&actionId=Siulo&returnurl=%2Fpatalpinti%2Fpasirinkti-kategorija")

driver.find_element(By.ID,'title-container').find_element(By.CLASS_NAME,'textbox').send_keys("Automobilis geras")
driver.find_element(By.CLASS_NAME,'resizable-textarea').find_element(By.ID, "text").send_keys("Automobilis nerealus")
driver.find_element(By.ID,'price-container').find_element(By.ID, "price").send_keys("666")
driver.find_element(By.ID,'phone-container').find_element(By.ID, "phone").send_keys("+37060011123")
driver.find_element(By.ID, "submit-button").click()

driver.find_element(By.ID, "inputfile").send_keys("/Users/erikas/Downloads/bmw-530-2-0-l-sedanas-2024-benzinas.jpg")
time.sleep(2)
# driver.find_element(By.ID, "back-button").click()
driver.find_element(By.ID, "forward-button").click()
driver.find_element(By.ID, "forward-button").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "action").click()

# https://elenta.lt/1303093/automobilis-geras - created ads

# driver.find_element(By.ID, "ad-edit-navigation-buttons-container").find_element(By.ID, "forward-button").click()

# driver.find_element(By.ID,'Email').send_keys("manopastas@pastas.lt")
# driver.find_element(By.ID,'Password').send_keys("Manopsw123")
# driver.find_element(By.ID,'Password2').send_keys("Manopsw123")
# driver.find_element(By.CLASS_NAME,'bigNavBtn2').click()

input()
driver.close()
driver.quit()

### ------------------- In functions #########

EMAIL = "manopastas@pastas.lt"
PASSWORD = "Manopsw123"
USERNAME = "sveikiLABA123"
PHOTO_PATH = "/Users/erikas/Downloads/bmw-530-2-0-l-sedanas-2024-benzinas.jpg"

def start_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

def accept_cookies(driver):
    driver.get("https://elenta.lt/")
    driver.find_element(By.CLASS_NAME, "fc-cta-consent").click()

def register_account(driver):
    driver.get("https://elenta.lt/registracija")
    driver.find_element(By.ID, 'UserName').send_keys(USERNAME)
    driver.find_element(By.ID, 'Email').send_keys(EMAIL)
    driver.find_element(By.ID, 'Password').send_keys(PASSWORD)
    driver.find_element(By.ID, 'Password2').send_keys(PASSWORD)
    driver.find_element(By.CLASS_NAME, 'bigNavBtn2').click()
    time.sleep(1)
    driver.find_element(By.ID, 'submit-new-ad-nav-button').click()

def create_ad(driver):
    driver.get("https://elenta.lt/patalpinti/pasirinkti-kategorija/automoto")
    driver.get("https://elenta.lt/patalpinti/ivesti-informacija?categoryId=AutoMoto_Automobiliai&actionId=Siulo")

    driver.find_element(By.ID, 'title-container').find_element(By.CLASS_NAME, 'textbox').send_keys("Automobilis geras")
    driver.find_element(By.CLASS_NAME, 'resizable-textarea').find_element(By.ID, "text").send_keys("Automobilis nerealus")
    driver.find_element(By.ID, 'price-container').find_element(By.ID, "price").send_keys("666")
    driver.find_element(By.ID, 'phone-container').find_element(By.ID, "phone").send_keys("+37060011123")
    driver.find_element(By.ID, "submit-button").click()

def upload_photo(driver):
    driver.find_element(By.ID, "inputfile").send_keys(PHOTO_PATH)
    time.sleep(2)
    driver.find_element(By.ID, "forward-button").click()
    driver.find_element(By.ID, "forward-button").click()
    time.sleep(2)

def finish(driver):
    driver.find_element(By.CLASS_NAME, "action").click()
    input()
    driver.quit()

# ——— Main ———
driver = start_driver()
accept_cookies(driver)
register_account(driver)
create_ad(driver)
upload_photo(driver)
finish(driver)
'''

## UZD 2 ##
'''
skelbiu.lt
nurinkti visas kainas šių prekių, bei konsolėje išspausdinti kokia prekės vidutinė kaina. 
1. TAS PATS KODAS TURI VEIKTI VISIEMS IEŠKOMIEMS ŽODŽIAMS.
2. KAINAS NURENKAME IŠ SKELBIMŲ VIDAUS. NE IŠORĖS. TAIP, UŽEINAT Į KORTELES IR IŠ TEN IMAT. NE, NETINKA IŠ BENDRO PUSLAPIO. EINAT Į KORTELES ;)
3. Nurenkam kainas tik tų skelbimų kurie yra tiesiogiai patalpinti į skelbiu.lt. cvbankas, kainos.lt, aruodas ir kiti nedomina, praleidžiam.
Paieškos žodžiai:
karpis
dezodorantas
bleebloo
samsung
'''

# def open_site():
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://skelbiu.lt/")
driver.find_element(By.ID, "onetrust-reject-all-handler").click()

driver.find_element(By.ID, "searchKeyword").send_keys("karpis")
driver.find_element(By.ID,"searchButton").click()

web_elements = driver.find_element(By.CLASS_NAME, "standard-list-container").find_elements(By.TAG_NAME, "a")



input()



