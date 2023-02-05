from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time
import datetime

category = ['Politics', 'Economic', 'Social', 'Culture', 'World', 'IT']     # 카테고리 6개
pages = [101, 101, 101, 71, 94, 73]                                         # 100페이지 까지만
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100#&date=%2000:00:00&page=2'

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('lang=kr_KR')
driver = webdriver.Chrome('./chromedriver', options=options)                # 크롬드라이버.exe 파일 필요
df_title = pd.DataFrame()


for i in range(4, 6):                # section  # 서현 : 섹션 5-World, 6-IT 맡음
                                     # i = 0~6(전체) => 4~6 (섹션 5, 6)
    titles = []
    for j in range(1, pages[i]):     # page
        url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}#&date=%2000:00:00&page={}'.format(i, j)
        driver.get(url)
        time.sleep(0.2)              # 페이지 열릴 때 time.sleep
        for k in range(1, 5):        # x_path  # 네이버는 1페이지당 기사 20개씩.
            for l in range(1, 6):    # x_path  # l=5개, k=4개 5*4 = 20개
                x_path = '//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt[2]/a'.format(k, l)
                         # '//*[@id="section_body"]/ul[1]/li[4]/dl/dt[1]/a/img'
                         # '//*[@id="section_body"]/ul[1]/li[5]/dl/dt/a'
                try:
                    title = driver.find_element('xpath', x_path).text
                    title = re.compile('[^가-힣 ]').sub(' ', title)
                    titles.append(title)
                except NoSuchElementException as e:
                    x_path = '//*[@id="section_body"]/ul[{}]/li[{}]/dl/dt/a'.format(k, l)
                    title = driver.find_element('xpath', x_path).text
                    title = re.compile('[^가-힣 ]').sub(' ', title)
                    titles.append(title)
                except:
                    print('error', i, j, k ,l)                              # 카테고리(섹션), 페이지, k, l
        if j % 10 == 0:                                                     # 10 페이지마다 저장
            df_section_title = pd.DataFrame(titles, columns=['titles'])     # 컬럼명 titles
            df_section_title['category'] = category[i]
            df_title = pd.concat([df_title, df_section_title], ignore_index=True)
            df_title.to_csv('./crawling_data/crawling_data_{}_{}.csv'.format(category[i], j), index=False)

            titles = []                                                     # 리스트 비워주기










