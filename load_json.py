
import json

with open('practice.json',encoding="utf-8") as f:
  data = json.load(f)

# 这就是个字典
print(type(data))

# 打印所有信息
print('=========')
print(data)

# 打印评价信息
print('=========')
print(data['evaluate'])

# 打印虾滑的评价
print('=========')
print(data['food'][2]['reason'])
