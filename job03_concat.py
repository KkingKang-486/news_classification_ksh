import pandas as pd
import glob
import datetime

data_path = glob.glob('./crawling_data/*.csv')                      # crawling_data 폴더 안에 있는 모든 파일 불러오기
print(data_path)
df = pd.DataFrame()
for path in data_path:
    df_temp = pd.read_csv(path)
    df = pd.concat([df,df_temp], ignore_index=True)
df.dropna(inplace=True)                  # 중복제거 추가 22.11.29
df.reset_index(inplace=True, drop=True)  # 22.11.29

df.dropna(inplace = True)
df.reset_index(inplace = True, drop = True)
print(df.head())

df.info()
df.to_csv('./crawling_data/naver_news_titles_{}.csv'.format(        # 컨캣한 파일 저장
    datetime.datetime.now().strftime('%Y%m%d')), index = False)