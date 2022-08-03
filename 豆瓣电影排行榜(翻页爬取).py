import requests
from lxml import etree
start_url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", }

# 抓取一页的数据
def get_one_page(url):
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)

    ranks = tree.xpath('//div[@class="item"]/div[1]/em/text()')
    names = tree.xpath('//div[@class="info"]/div[1]/a/span[1]/text()')
    scores = tree.xpath('//div[@class="star"]/span[2]/text()')

    movies = list(zip(ranks, names, scores))
    return movies

#抓取所有数据
def get_all_pages():
    all_movies =[]
    start_num = 0
    for i in range(1,11): #循环10次
        url = f"https://movie.douban.com/top250?start={start_num}&filter=" #格式化字符串
        print(f"开始爬取第{i}页")
        movies = get_one_page(url)
        all_movies.append(movies)
        start_num = start_num + 25
    print("250条数据爬取完毕")
    return all_movies
print(get_all_pages()) 