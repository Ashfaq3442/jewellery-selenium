from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import pandas as pd
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()
driver.get("https://cullenjewellery.com/engagement-rings")

data=[]

for i in range(1,40):
    price=Review=Ring_Name=Avg=Average_band_width=Carat_Total_Weight=center_stone_size=None
    link=driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/main/div/div[5]/div[2]/div/div[3]/ul/li[{i}]/a")
    product_url = link.get_attribute("href")
    driver.get(product_url)



    try:
        price=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[2]/p").text
    except NoSuchElementException:
        price="N/A"

    try:
        Review=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[1]/a/div/div[7]/div").text
    except NoSuchElementException:
        Review="N/A"

    try:
        Ring_Name=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/h1").text
    except NoSuchElementException:
        Ring_Name="N/A"
    Detail_find_element=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/button/div[2]").click()

    try:
        Avg=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[1]/td").text
    except NoSuchElementException:
        Avg="N/A"

    try:
        Carat_Total_Weight=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[2]/td").text
    except NoSuchElementException:
        Carat_Total_Weight="N/A"

    try:
        Average_band_width=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[3]/td").text
    except NoSuchElementException:
        Average_band_width="N/A"

    try:
        center_stone_size=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[4]/td").text
    except NoSuchElementException:
        center_stone_size="N/A"

    data.append({
    "Ring Name" : Ring_Name,
    "Price : ":price,
    "Review :":Review,
    "Avg. No. Side Stones" :Avg,
    "Carat Weight" :Carat_Total_Weight,
    "Average Band Width :":Average_band_width,
    "Center Stone Size :":center_stone_size,
    })

    # print("................\n\n\n\n")
    # print("Ring Name :", Ring_Name)
    # print("Price : ",price)
    # print("Review :",Review)
    # print("Avg. No. Side Stones :",Avg)
    # print("Carat Weight :",Carat_Total_Weight)
    # print("Average Band Width :",Average_band_width)
    # print("Center Stone Size :", center_stone_size)
    # print("................\n\n\n\n")
    time.sleep(3)
    driver.back()
    time.sleep(3)
df=pd.DataFrame(data)
df.to_csv("engagement_rings.csv", index=False, encoding='utf-8', sep=',')
driver.quit