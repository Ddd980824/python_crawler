import requests
from lxml import etree
import os
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
# url1 = "https://www.qbiqu.com/0_899/"  # 编码为"gbk"
# 解决乱码问题
# 乱码的原因通常只有⼀个：编码和解码⽤了不同的规则。


def get_index(url):
    res = requests.get(url, headers=headers)
    # 指定编码格式
    #res.encoding = "gbk"
    tree = etree.HTML(res.text)
    name = tree.xpath('//div[@id="info"]/h1/text()')[0]  # 爬取小说的名字
    link = tree.xpath('//div[@id="list"]/dl/dd/a/@href')  # 爬取小说章节的连接
    title = tree.xpath('//div[@id="list"]/dl/dd/a/text()')  # 爬取小说章节的标题
    catalog = list(zip(link, title))
    print(f"小说的名字是：{name}")
    return name, catalog


# 创建文件夹，且以小说名字命名
def creat_folder(folder_name):
    if not os.path.exists(folder_name):
        print("文件夹不存在，创建文件夹")
        os.makedirs(folder_name)

    else:
        print("文件夹已存在")
    # 切换到文件夹中
    os.chdir(folder_name)


# 保存章节内容
def get_unit(title, url):
    rs = requests.get(url, headers=headers)
    tree = etree.HTML(rs.text)
    paras = tree.xpath('//div[@id="content"]/text()')  # 爬取小说的内容
    # strip()方法去除元素前后的空格或回车
    paras = [p.strip() for p in paras]
    content = "\n".join(paras)
    print(f"开始保存：{title}")
    with open(f"{title}.txt", "w", encoding="utf8") as f:
        f.write(title + "\n\n")
        f.write(content)
        print(title+"保存成功")

# 创建主函数和用户交互，组装和调用之前的函数实现完整功能


# 网址的域名地址，用来拼接完整的URL
base_url = "https://www.hongyue8.com"


# 爬虫的主函数
def main():
    url = input("请输入要抓取小说的地址: ")
    name, catalog = get_index(url)
    creat_folder(name)

    for cata in catalog:
        full_link = base_url + cata[0]
        title = cata[1]
        get_unit(title, full_link)
    print("全部下载完成！")


# 魔法变量保证只有在直接运⾏这个脚本的时候才会执⾏if块中的main函数
if __name__ == "__main__":
    main()

# 绝对路径下新建文件夹
# os.makedirs(r"D:\科研数据处理\立方数据学社\python城市数据爬取\python城市数据爬取练习\绝对路径test")
# 编码和解码
# print("柠檬酸奶".encode("gbk"))
# print("柠檬酸奶".encode("utf8"))
# print(b'\xc4\xfb\xc3\xca\xcb\xe1\xc4\xcc'.decode('gbk'))
# print(b'\xe6\x9f\xa0\xe6\xaa\xac\xe9\x85\xb8\xe5\xa5\xb6'.decode("utf8"))
