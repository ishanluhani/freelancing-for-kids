import pandas, time
from selenium import webdriver
driver = webdriver.Edge("msedgedriver.exe")
codes = []
file = open('data.txt', 'w')
for i in range(16):
    a = driver.get(f'https://www.codechef.com/practice?end_rating=999&group=unattempted&hints=0&itm_campaign=practice&itm_medium=navmenu&limit=20&page={i}&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=0&tags=&topic=&video_editorial=0&wa_enabled=0')
    time.sleep(2)
    codes.extend(list(pandas.read_html(driver.page_source)[0]['Code']))
file.write(','.join(codes))