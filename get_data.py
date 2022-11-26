import pandas, time
from selenium import webdriver
driver = webdriver.Edge("msedgedriver.exe")
codes = []
file = open('data_for_me.txt', 'w')
for i in range(8):
    a = driver.get(f'https://www.codechef.com/practice?end_rating=1299&group=unattempted&hints=0&itm_campaign=practice&itm_medium=navmenu&limit=20&page={i}&search=&sort_by=difficulty_rating&sort_order=asc&start_rating=1200&tags=&topic=&video_editorial=0&wa_enabled=0')
    time.sleep(2)
    codes.extend(list(pandas.read_html(driver.page_source)[0]['Code']))
file.write(','.join(codes))