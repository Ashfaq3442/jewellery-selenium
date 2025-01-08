from selenium import webdriver



from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import pandas as pd
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()
driver.get("https://cullenjewellery.com/engagement-rings")
for i in range(1,10):
    link=driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/main/div/div[5]/div[2]/div/div[3]/ul/li[{i}]/a")
    product_url = link.get_attribute("href")
    driver.get(product_url)



    try:
        price=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[2]/p").text
    except FileNotFoundError:
        pass

    try:
        Review=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[1]/a/div/div[7]/div").text
    except FileNotFoundError:
        pass

    try:
        Ring_Name=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/h1").text
    except FileNotFoundError:
        pass
    Detail_find_element=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/button/div[2]").click()

    try:
        Avg=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[1]/td").text
    except FileNotFoundError:
        pass

    try:
        Carat_Total_Weight=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[2]/td").text
    except FileNotFoundError:
        pass

    try:
        Average_band_width=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[3]/td").text
    except FileNotFoundError:
        pass

    try:
        center_stone_size=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[4]/td").text
    except FileNotFoundError:
        pass
    print("................\n\n\n\n")
    print("Ring Name :", Ring_Name)
    print("Price : ",price)
    print("Review :",Review)
    print("Avg. No. Side Stones :",Avg)
    print("Carat Weight :",Carat_Total_Weight)
    print("Average Band Width :",Average_band_width)
    print("Center Stone Size :", center_stone_size)
    print("................\n\n\n\n")
    time.sleep(7)
    driver.back()
    time.sleep(3)








# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import time

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver.maximize_window()
# driver.get("https://cullenjewellery.com/engagement-rings")
# # Loop through the products
# for i in range(1, 10):
#         link = driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/main/div/div[5]/div[2]/div/div[3]/ul/li[{i}]/a")
#         product_url = link.get_attribute("href")
#         driver.get(product_url)

#         try:
#             ring_name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/h1").text
#         except NoSuchElementException:
#             pass

#         try:
#             price = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[2]/p").text
#         except NoSuchElementException:
#             pass

#         try:
#             review = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[1]/a/div/div[7]/div").text
#         except NoSuchElementException:
#             pass

#         detail_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/button/div[2]")
#         detail_button.click()
        

#         try:
#             avg = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[1]/td").text
#         except NoSuchElementException:
#             pass

#         try:
#             carat_total_weight = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[2]/td").text
#         except NoSuchElementException:
#             pass

#         try:
#             average_band_width = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[3]/td").text
#         except NoSuchElementException:
#             pass

#         try:
#             center_stone_size = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[4]/td").text
#         except NoSuchElementException:
#             pass

#         # Print the details
#         print("................\n")
#         print("Ring Name :", ring_name)
#         print("Price :", price)
#         print("Review :", review)
#         print("Avg. No. Side Stones :", avg)
#         print("Carat Weight :", carat_total_weight)
#         print("Average Band Width :", average_band_width)
#         print("Center Stone Size :", center_stone_size)
#         print("................\n")

#         time.sleep(7)
#         driver.back()
#         time.sleep(3)
