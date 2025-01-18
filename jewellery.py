from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import requests

import time
import pandas as pd
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
driver.maximize_window()
driver.get("https://cullenjewellery.com/engagement-rings")


image_folder="Ring Images"
os.makedirs(image_folder,exist_ok=True)

def sanitize_folder_name(name):
    return "".join(c if c.isalnum() or c in " _-" else "_" for c in name)

data=[]

for i in range(1,51):
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

    folder_name = sanitize_folder_name(Ring_Name)
    ring_image_folder = os.path.join(image_folder, folder_name)
    os.makedirs(ring_image_folder, exist_ok=True)

    try:
        for j in range(1,10):
            image_element=driver.find_element(By.XPATH,f"/html/body/div[1]/div[1]/main/div/div/div/div[1]/div/div/div/div[3]/button[{j}]/div[1]/div/div/img")
            image_url=image_element.get_attribute("src")
            image_file_name=os.path.join(ring_image_folder, f"ring{j}.jpg")
            response=requests.get(image_url, stream=True)
            if response.status_code==200:
                with open (image_file_name, "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                impage_path=image_file_name
            else:
                impage_path= "Image Download Failed"
    except NoSuchElementException:
        impage_path="N/A"


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
    time.sleep(7)
    driver.back()
    time.sleep(5)
df=pd.DataFrame(data)
df.to_csv("engagement_rings.csv", index=False, encoding='utf-8', sep=',')
driver.quit



# import os
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

# import time
# import pandas as pd

# # Setup Chrome options and driver
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver.maximize_window()
# driver.get("https://cullenjewellery.com/engagement-rings")

# # Create a folder to save images
# image_folder = "ring_images"
# os.makedirs(image_folder, exist_ok=True)

# # List to store product data
# data = []

# for i in range(1, 20):
#     price = Review = Ring_Name = Avg = Average_band_width = Carat_Total_Weight = center_stone_size = Image_Path = None
    
#     link = driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/main/div/div[5]/div[2]/div/div[3]/ul/li[{i}]/a")
#     product_url = link.get_attribute("href")
#     driver.get(product_url)

#     try:
#         price = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[2]/p").text
#     except NoSuchElementException:
#         price = "N/A"

#     try:
#         Review = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[1]/a/div/div[7]/div").text
#     except NoSuchElementException:
#         Review = "N/A"

#     try:
#         Ring_Name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/h1").text
#     except NoSuchElementException:
#         Ring_Name = "N/A"

#     Detail_find_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/button/div[2]").click()

#     try:
#         Avg = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[1]/td").text
#     except NoSuchElementException:
#         Avg = "N/A"

#     try:
#         Carat_Total_Weight = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[2]/td").text
#     except NoSuchElementException:
#         Carat_Total_Weight = "N/A"

#     try:
#         Average_band_width = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[3]/td").text
#     except NoSuchElementException:
#         Average_band_width = "N/A"

#     try:
#         center_stone_size = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/section/div[6]/div[1]/div/div/table/tr[4]/td").text
#     except NoSuchElementException:
#         center_stone_size = "N/A"

#     # Download and save the image
#     try:
#         image_element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/div/div/div[1]/div/div/div/div[3]/button[1]/div[1]/div/div/img")
#         image_url = image_element.get_attribute("src")

#         # Generate a filename and save the image
#         image_filename = os.path.join(image_folder, f"ring_{i}.jpg")
#         response = requests.get(image_url, stream=True)
#         if response.status_code == 200:
#             with open(image_filename, 'wb') as file:
#                 for chunk in response.iter_content(1024):
#                     file.write(chunk)
#             Image_Path = image_filename
#         else:
#             Image_Path = "Image download failed"
#     except NoSuchElementException:
#         Image_Path = "N/A"

#     # Append extracted data to list
#     data.append({
#         "Ring Name": Ring_Name,
#         "Price": price,
#         "Review": Review,
#         "Avg. No. Side Stones": Avg,
#         "Carat Weight": Carat_Total_Weight,
#         "Average Band Width": Average_band_width,
#         "Center Stone Size": center_stone_size,
#         "Image Path": Image_Path
#     })

#     time.sleep(7)
#     driver.back()
#     time.sleep(3)

# # Save data to a CSV file
# df = pd.DataFrame(data)
# df.to_csv("engagement_rings_with_images.csv", index=False, encoding='utf-8', sep=',')

# driver.quit()

# print("Data scraping completed. Images saved in 'ring_images' folder. Data saved in 'engagement_rings_with_images.csv'.")
