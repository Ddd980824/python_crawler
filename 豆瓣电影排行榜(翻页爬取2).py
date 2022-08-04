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
    next_url = tree.xpath('//span[@class="next"]/a/@href')

    movies = list(zip(ranks, names, scores))
    return movies,next_url

#抓取所有数据
def get_all_pages2():
    all_movies =[]
    current_url = start_url
    while(current_url):
        movies,next_url = get_one_page(current_url)
        all_movies.append(movies)
        if len(next_url) > 0:
            current_url = start_url + next_url[0]
            print(f"下一页地址是：{current_url}")
        else:
            current_url = None
            print("没有下一页了，抓取结束！")
    return all_movies
print(get_all_pages2())
