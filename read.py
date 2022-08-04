# 读入文件并一次性读出所有内容
with open("write.txt", "r") as f:
    text = f.read()
    print(text,end="")

print("==============================")

# 一次性读出所有并返回一个列表
with open("write.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line,end="")


print("==============================")

# 一次性读出一行
with open("write.txt", "r") as f:
    line = f.readline()
    while(line):
        print(line, end="")
        line = f.readline()

print("==============================")

#绝对路径下读入文件
with open("D:\科研数据处理\立方数据学社\python城市数据爬取\python城市数据爬取练习\\write.txt","r") as f:
    txt = f.read()
    print(txt,end="")