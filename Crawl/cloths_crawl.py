import requests
from bs4 import BeautifulSoup

url = 'https://www.aroundthecorner.com/shop/list.php?cate=0201'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

li_list = soup.select('#ABox > div.contents > div > div.content-inner.clearfix > div.content-wrap.pull-left > div.basic.product-list-wrap.type-a.relative > ul> li')

for li in li_list:
    img_tag = li.select('div a img')
    product_name = img_tag[0].attrs['alt']
    image_url = img_tag[0].attrs['src']

    print('상품명: ', product_name)
    print('url: ', image_url)