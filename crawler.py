#%%
from selenium import webdriver
import csv
import os

#%%
url = "https://www.youtube.com/watch?v=lGCo8ILvauI&t=1785s"

#%%
# 창 안 띄우기
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(os.getcwd() + '/chromedriver', chrome_options=options)
#%%
driver.get(url)
driver.implicitly_wait(0.3)

#%%
youtube_xpath_meta = {
    'title' : """//*[@id="container"]/h1/yt-formatted-string""",
    'views' : """//*[@id="count"]/yt-view-count-renderer/span[1]""",
    'date' : """//*[@id="date"]/yt-formatted-string"""
}

#%%
print("Crawler start...")

crawled_data = {}

for _type, _xpath in youtube_xpath_meta.items():
    print(f"Let's get {_type} !!")
    crawled_data[_type] = driver.find_element_by_xpath(f"{_xpath}").text
    driver.implicitly_wait(0.3)
    
    print(f"contents : {crawled_data[_type]}")
    print()

driver.quit()
print("Crawler end...")

# %%
with open('results1.csv', 'w') as f:
    w = csv.DictWriter(f, crawled_data.keys())
    w.writeheader()
    w.writerow(crawled_data)