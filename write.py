#Python 创建文件并写入
with open("write.txt","w") as f:
    for i in range(1,11):
        f.write(f'{i}\n')