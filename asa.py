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
driver.get("https://www.flipkart.com/search?q=smart+watch&sid=ajy%2Cbuh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=smart+watch%7CSmart+Watches&requestId=a3a0ac86-976b-49e7-b440-ae427f9159e9&as-backfill=on&otracker=nmenu_sub_Electronics_0_Smart+Watches&page=1")
watch_name=[]
Rating=[]
Review=[]
price=[]
for j in range (2,3):
    for i in range(1,5):
        link=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{j}]/div/div[{i}]/div/div/a[1]")
        product_url = link.get_attribute("href")  # Extract the href link
        # print(f"Product URL: {product_url}")
        driver.get(product_url)
        watch_name_element=driver.find_element(By.CLASS_NAME,"VU-ZEz")
        watch_name.append(watch_name_element.text)
        Rating_element=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[1]")
        Rating.append(Rating_element.text)
        Review_element=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[3]")
        Review.append(Review_element.text)
        Price_element=driver.find_element(By.CLASS_NAME,"Nx9bqj ")
        price.append(Price_element.text)
        

        # print("....................................\n\n\n\n")
        # print("watch Name:",watch_name)
        # print("Rating:",Rating)
        # print("Review:",Review)
        # print("Price:",price)
        driver.back()
        time.sleep(6)


Next_Page_element=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]/span").click()

for k in range (2,4):
    for j in range (2,3):
        for i in range(1,5):
            link=driver.find_element(By.XPATH,f"/html/body/div/div/div[3]/div[1]/div[2]/div[{j}]/div/div[{i}]/div/div/a[1]")
            product_url = link.get_attribute("href")  # Extract the href link
            # print(f"Product URL: {product_url}")
            driver.get(product_url)
            watch_name_element=driver.find_element(By.CLASS_NAME,"VU-ZEz")
            watch_name.append(watch_name_element.text)
            Rating_element=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[1]")
            Rating.append(Rating_element.text)
            Review_element=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]/span/span[3]")
            Review.append(Review_element.text)
            Price_element=driver.find_element(By.CLASS_NAME,"Nx9bqj ")
            price.append(Price_element.text)

            # print("....................................\n\n\n\n")
            # print("watch Name:",watch_name)
            # print("Rating:",Rating)
            # print("Review:",Review)
            # print("Price:",price)
            driver.back()
            time.sleep(6)
    Next_Page_element=driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[12]/span").click()

Data_Records={"watch_name": watch_name, "Rating":Rating, "Review":Review, "price":price}
df=pd.DataFrame(Data_Records)
df.to_csv("Watches on flipkart", index=False )