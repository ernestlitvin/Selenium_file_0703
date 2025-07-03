import time

from selenium.webdriver.common.by import By
from selenium import webdriver

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


# driver.find_element(By.ID, "ad-edit-navigation-buttons-container").find_element(By.ID, "forward-button").click()










# driver.find_element(By.ID,'Email').send_keys("manopastas@pastas.lt")
# driver.find_element(By.ID,'Password').send_keys("Manopsw123")
# driver.find_element(By.ID,'Password2').send_keys("Manopsw123")
# driver.find_element(By.CLASS_NAME,'bigNavBtn2').click()





input()
driver.close()
driver.quit()





