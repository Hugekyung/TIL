from selenium import webdriver
from bs4 import BeautifulSoup
import time, os
from datetime import datetime
import pandas as pd

# review link link
# 리지니2M
link = 'https://play.google.com/store/apps/details?id=com.ncsoft.lineage2m19&showAll&showAllReviews=true'

# 몇 번 스크롤 할건지
scroll_cnt = 15

# download chrome driver https://sites.google.com/a/chromium.org/chromedriver/home
driver = webdriver.Chrome('C:/Users/haech/chromedriver.exe')
driver.get(link)

# os.makedirs('result', exist_ok=True) # 결과 폴더 생성

for i in range(scroll_cnt):
  print('스크롤 {} 번째 진행 중'.format(i+1))
  # scroll to bottom
  driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
  time.sleep(3)

  # click 'Load more' button, if exists
  try:
    
    load_more = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div/span/span')
    load_more.click()
    print('button click!!!')
  except:
    print('Cannot find load more button...')

# get review containers
reviews = driver.find_elements_by_xpath('//*[@jsname="fk8dgd"]//div[@class="d15Mdf bAhLNe"]')

print('There are %d reviews avaliable!' % len(reviews))
print('Writing the data...')

# create empty dataframe to store data
df = pd.DataFrame(columns=['name', 'ratings', 'date', 'helpful', 'comment'])

# get review data
for review in reviews:
  # parse string to html using bs4
  soup = BeautifulSoup(review.get_attribute('innerHTML'), 'html.parser')

  # reviewer
  name = soup.find(class_='X43Kjb').text

  # rating
  ratings = int(soup.find('div', role='img').get('aria-label').replace('별표 5개 만점에', '').replace('개를 받았습니다.', '').strip())

  # review date
  date = soup.find(class_='p2TkOb').text
  date = datetime.strptime(date, '%Y년 %m월 %d일')
  date = date.strftime('%Y-%m-%d')

  # helpful
  helpful = soup.find(class_='jUL89d y92BAb').text
  if not helpful:
    helpful = 0
  
  # review text
  comment = soup.find('span', jsname='fbQN7e').text
  if not comment:
    comment = soup.find('span', jsname='bN97Pc').text
  
  # developer comment
  # developer_comment = None
  # dc_div = soup.find('div', class_='LVQB0b')
  # if dc_div:
  #   developer_comment = dc_div.text.replace('\n', ' ')
  
  # append to dataframe
  df = df.append({
    'name': name,
    'ratings': ratings,
    'date': date,
    'helpful': helpful, # 좋아요 수
    'comment': comment
    # 'developer_comment': developer_comment
  }, ignore_index=True)

# finally save the dataframe into csv file
# filename = datetime.now().strftime('result/%Y-%m-%d_%H-%M-%S.csv')
filename = 'lineage2m.csv'
df.to_csv(filename, encoding='utf-8-sig', index=False)
driver.stop_client()
driver.close()

print('Done!')