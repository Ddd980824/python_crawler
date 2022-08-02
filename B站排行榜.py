import requests

from lxml import etree  # 导入支持xpath路径表达的包

url = "https://www.bilibili.com/v/popular/rank/all"

res = requests.get(url)

# 检查一下是否成功获取html
# print(res.status_code)
# print(res.headers)
# print(res.text)

tree = etree.HTML(res.text)  # 实例化并解析网页源代码为一个对象

P = tree.xpath('//p/text()')

print(P)
print('===================')
# 爬取视频排名及名称
ranks = tree.xpath('//ul[@class="rank-list"]/li/div/div[1]/i/span/text()')

print(ranks)
print('===================')
names = tree.xpath("//ul[@class='rank-list']/li/div/div[2]/a/text()")

print(names)
print('===================')
#数据处理
data = dict(zip(ranks,names))

#检查数据合适合并成功
# print(data)

#按排名加视频名称的形式打印
for r in data:
    print(r,data[r])
