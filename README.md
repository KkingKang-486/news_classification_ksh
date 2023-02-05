# news_classification_ksh


이 저장소의 파이썬 실행버전은 3.7입니다.



폴더구조<br>
project_root --- crawling_data <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- models<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- temp<br>


<br><br><br>
# 프로젝트 소개
네이버 뉴스 카테고리 분류를 위한 프로젝트<br>

## 프로젝트 설명
* 카테고리 :  'Politics', 'Economic', 'Social', 'Culture', 'World', 'IT' 6개로 분류되어있습니다 <br>
* 크롤링 : job01 - 모델 예측 시 테스트로 쓰일 data (당일의 뉴스 헤드라인) <br>
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;job02 - 카테고리 1개당(100페이지 이내로 제한) csv 파일이 만들어지며, 컨캣한 파일은 naver_news_titles_{날짜}로 저장됩니다 <br>
* 만들어지는 모델 : 'news_category_classfication_model_0.993.h5', 'news_data_max_20_wordsize_11919.npy' 파일이 만들어집니다 <br>

## 필요한 파일
* 필요한 파일 : 같은 폴더 내에 'chromedriver.exe', 'stopwords.csv', ('requirements.txt') 가 필요합니다 <br>
              models 폴대 내에 'labled_encoder.pickle', 'news_token_pickle' 파일이 필요합니다 <br>
