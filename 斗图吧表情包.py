from lxml import etree
import requests


def download_pic(pic_name, pic_url, pic_type):
    '''
    :pic_name 表情包的名字
    :pic_url  表情包的url
    :pic_type 表情包文件的后缀
    '''
    print(f"dowmloading...{pic_url}")
    file_name = f"pics/{pic_name}.{pic_type}"
    rs = requests.get(pic_url, headers=headers)
    with open(file_name, "wb") as f:
        f.write(rs.content)
        print(f"下载成功{pic_url}")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
doutu_url = "http://doutu8.net/pic/taotu.html"
res = requests.get(doutu_url, headers=headers)
tree = etree.HTML(res.text)
# 使用xpath 提取图片所在的a标签
item_list = tree.xpath('//ul[@class="related_img"]/li/a')
for item in item_list:
    # 图片的名称
    pic_name = item.xpath('./img/@alt')[0]

    # 图片的链接
    pic_link = item.xpath('./img/@src')[0]
    pic_url = "http:"+pic_link

    # 图片的类型
    type_start = pic_link.rfind(".")+1  # rfind() 返回字符串最后一次出现的索引，如果没有匹配项则返回-1
    pic_type = pic_link[type_start:]
    download_pic(pic_name, pic_url, pic_type)
