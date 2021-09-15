""" 파이썬 데이터 읽고 쓰기
pickle
- pickle은 텍스트가 아닌 파이썬 자료형을 읽고 쓸 수 있게 해주는 라이브러리.
- 파이썬 자료형을 형태변환 없이 그대로 저장할 수 있다.
- open('text.txt', 'W') 방식으로 입력할 경우에는 String 자료형으로 저장된다.
- pickle로 데이터를 저장하거나 불러올 경우 바이트 형식으로 읽거나 써야한다.(rb, wb)


(참고)파일 읽어올 때, 경로 앞에 'r'의 역할
- r은 'raw'의 약자로 해당 문자열이 원시 문자열임을 나타내는 것.
- 백슬래시를 해석하지 않는다.
"""
import pandas as pd
import pickle as pk
import os

df = pd.read_csv('D:kmong/instagram_dashboard/influencer_re.csv')
username_lst = list(df['username']) # 리스트 자료형

# 파일 쓰기 with pickle --> 리스트 자료형 그대로 저장한다.
# with open('Python_basic/username.txt', 'wb') as f:
#     pk.dump(username_lst, f)

# 파일 읽기 with pickle --> 리스트 자료형 그대로 읽어온다.
# with open('Python_basic/username.txt', 'rb') as f:
#     data = pk.load(f)

# print(data)

# 해당 경로에 찾고자 하는 파일이 존재하는지 확인
print(os.path.exists('Python_basic/username.txt'))

