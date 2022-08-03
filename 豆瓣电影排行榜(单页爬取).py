import requests
from lxml import etree
url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", }
res = requests.get(url, headers=headers)
print(res.status_code)
# print(res.text) #查看html

# 爬取排名
tree = etree.HTML(res.text)
ranks = tree.xpath('//div[@class="item"]/div[1]/em/text()')
print(ranks)
print("***********************************************")
# 爬取电影名称
names = tree.xpath('//div[@class="info"]/div[1]/a/span[1]/text()')
print(names)
print("***********************************************")
# 爬取电影经典台词
abstract = tree.xpath('//p[@class="quote"]/span/text()')
print(abstract)
print("***********************************************")
# 爬取评分
scores = tree.xpath('//div[@class="star"]/span[2]/text()')
print(scores)
print("================================================")
# 数据组装
movie = list(zip(ranks, names, abstract, scores))
print(movie)
