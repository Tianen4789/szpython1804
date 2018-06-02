
# 字符串 ： 使用引号（双引号或单引号）包裹的内容就是字符串

name = "宝强"
age = 33
sex = '爷们'

# "宝强是'爷们'"

# + ：字符串连接
# 如果是变量，那就不要加引号
print("name + age + sex")
print(name + str(age) + sex)

# * ：重复
print(name + " very "*3 + sex)


# 获取字符串中的字符
myStr = "I like LOL"
# 下标/索引 ： 从0开始
print(myStr[0])  # 'I'
print(myStr[1])  # ' '
print(myStr[2])  # 'l'
# print(myStr[100])  # 下标越界， 报错： IndexError: string index out of range
print(myStr[-2])  # 倒数第2个

# 字符串长度: len()
print(len(myStr))  # 10


# 截取字符串： 切片
myStr = "I like LOL"

print(myStr[:])  # "I like LOL"
print(myStr[3:])  # "ike LOL"
print(myStr[:8])  # "I like L", 不包含下标8的字符
print(myStr[3:8])  # "ike L"
print(myStr[2:6])  # "like"