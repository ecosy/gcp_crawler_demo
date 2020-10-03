from selenium import webdriver
import csv
import os

url = "https://www.youtube.com/watch?v=lGCo8ILvauI&t=1785s"

# 크롬 드라이버 권한 변경
os.chmod('./chromedriver', 755)

# 크롬 드라이버 창 안 띄우기 설정
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome(os.getcwd() + '/chromedriver', chrome_options=options)


# __________________________________________________________________________

# 이 아래 부분의 코드에 원하시는 크롤링 코드를 넣어 사용하시면 됩니다.
# __________________________________________________________________________


# url 접속하기
driver.get(url)
driver.implicitly_wait(0.3)

youtube_xpath_meta = {
    'title' : """//*[@id="container"]/h1/yt-formatted-string""",
    'views' : """//*[@id="count"]/yt-view-count-renderer/span[1]""",
    'date' : """//*[@id="date"]/yt-formatted-string"""
}

# xpath 사용해 크롤하기
print("Crawler start...")
crawled_data = {}

for _type, _xpath in youtube_xpath_meta.items():
    print("Let's get ", _type)
    crawled_data[_type] = driver.find_element_by_xpath(_xpath).text
    driver.implicitly_wait(0.3)
    
    print("contents :", crawled_data[_type])
    print()

driver.quit()
print("Crawler end...")

# csv 형태로 저장
with open('results1.csv', 'w') as f:
    w = csv.DictWriter(f, crawled_data.keys())
    w.writeheader()
    w.writerow(crawled_data)