import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://skelbiu.lt")
# time.sleep(5) #palaukia fiksuota laika

driver.find_element(By.ID,"onetrust-reject-all-handler").click()
driver.find_element(By.ID,'searchKeyword').send_keys("vaiku stovykla")
driver.find_element(By.ID,'searchButton').click()
time.sleep(5)
web_elements = driver.find_element(By.CLASS_NAME,'standard-list-container').find_elements(By.TAG_NAME,"a")
print(len(web_elements))
for a in web_elements:
    try:
        print(a.get_attribute("href"))
    except:
        pass

# /html/body/div[3]/div/div[1]/div[1]/form/div[3]/div[1]/a[10]
# //*[@id="popular_categories_by_keyword"]/a[10]
#                                //*[@id="item_prices-54xc42v"]/div/div[2]/div[1]/div[4]/a
#                    //*[@id="prices-container"]/div/section[1]/div/div[2]/div[1]/div[4]/a
# /html/body/div[2]/div[2]/div[3]/div[1]/article/div/section[1]/div/div[2]/div[1]/div[4]/a
print("hm...")
input()
driver.close()
driver.quit()
# def magic_function():
#     pass
# is_done = False
# while not is_done:
#     try:
#         is_done = magic_function()
#     except:
#         print()