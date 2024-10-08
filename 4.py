import requests
from bs4 import BeautifulSoup

# 获取百度热搜页面内容
url = 'https://top.baidu.com/board?tab=realtime'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

# 解析页面内容
soup = BeautifulSoup(response.text, 'html.parser')

# 查找热搜数据
hot_searches = soup.find_all('div', class_='c-single-text-ellipsis')

# 打印热搜标题和链接
for search in hot_searches:
    title = search.get_text().strip()
    link = f"https://www.baidu.com/s?wd={title}"
    print(f"热搜标题: {title}")
    print(f"链接: {link}")
    print("***\n")
