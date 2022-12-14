# Python基础04-容器类型、函数

[TOC]

## 能力目标

- [ ] 能够说出定义字典的基本格式{}
- [ ] 能够通过键对字典进行添加/修改元素操作
- [ ] 能够使用两个单引号、双引号、三引号定义字符串
- [ ] 能够使用字符串的常用操作方法
- [ ] 能够使用切片语法获取字符串指定区间内的子串



## 关卡一：基础题

### 1. 什么是KeyError？

**参考答案**

```python
键错误，字典中没有该键
```

### 2. 字符串切片的语法是什么？

**参考答案**

```python
字符串[开始索引:结束索引:步长]
```

## 关卡二：综合题

### 1. 设计一个程序

 按下述步骤实现代码:

- 创建一个空字典{}，变量名为 info

- 向字典 info 中添加新的键值对，保存如下信息：姓名是张三

- 获取字典中元素 name 的值

- 修改字典中的元素 'name' 的值为 '李四'

- 存在字典 info = {'name':'李四'}, 删除元素 name

**参考答案**

```python
# 创建一个空字典{}，变量名为 info
info = {}

# 向字典 info 中添加新的键值对，保存如下信息：姓名是张三
info['name'] = '张三'

# 获取字典中元素 name 的值
print(info['name'])

# 修改字典中的元素 'name' 的值为 '李四'
info['name'] = '李四'

# 存在字典 info = {'name':'李四'}, 删除元素 name
info.pop('name')
print(info)
```



### 2. 设计一个程序:

- 要求用户输入一个字符串，遍历当前字符串并打印，如果遇见“q”,则跳出循环。如果遇见“ ”（空格）则跳过当前输出。

**参考答案**

```python
str = input('输入一个字符串：')
print(str)

for i in input_str:
    if i == "q":
        break
    elif i == " ":
        continue
    print(i)
  

```

### 3. 设计一个程序

已知变量如下：

```
 a = "itheima"
```

- 从键盘上输入一个字母，判断此字母 是否在变量 a 中，如果在则输出 找到了， 如果不在 则输出 查无此字母

**参考答案**

```python
a = "itheima"

b = input('请输入一个字母：')

for c in a ：
if c == b:
  print('找到了')
  break
else:
    print('查无此字')
```

### 4. 设计一个程序

现有字典`dict1 = {'name':'chuanzhi','age':18}` 要求：

- 1.使用循环将字典中所有的键输出到屏幕上 
- 2.使用循环将字典中所有的值输出到屏幕上 
- 3.使用循环将字典中所有的键值对输出到屏幕上 输出方式： name：chuanzhi age:18

**参考答案**

```python
dict1 = {'name':'chuanzhi','age':18}
# 1.使用循环将字典中所有的键输出到屏幕上
for key in dict1:
    print(key)
# 2.使用循环将字典中所有的值输出到屏幕上 
for value in dict1.values():
    print(value)
# 3.使用循环将字典中所有的键值对输出到屏幕上
for key, vaule in dict1.items() :
  print(key,':',vaule, end='')

```

## 关卡三：扩展题

### 1. 设计一个程序

有这样的一个列表

```python
product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]
```

然后小明一共有8000块钱，那么他能不能买下这所有商品？ 如果能，请输出“能”，否则输出“不能”

**参考答案**

```python
product = [
    {"name": "电脑", "price": 7000},
    {"name": "鼠标", "price": 30},
    {"name": "usb电动小风扇", "price": 20},
    {"name": "遮阳伞", "price": 50},
]

money = int(input('你有多少钱：'))
sum_price= 0

for product_dict in product : # 先遍历列表，把列表中的每个元素赋值给product_dict(字典)
    price = product_dict['price']
    sum_price += price

print('电脑总价是:%d' % sum_price)

if money >= sum_price :
    print('你可以买！')
else:
    print('你钱不够！')
```

### 2. 设计一个程序

- 现有字符串如下，请使用切片提取出ceg
  words = "abcdefghi"

**参考答案**

```python
words = "abcdefghi"
res = words[2:7:2]
print(res)
```

### 3. 设计一个程序

现有字符串： str1 = '1234567890'，根据题目要求，将截取后的新字符串赋值给str2

- 截取字符串的第一位到第三位的字符：`123`
- 截取字符串最后三位的字符：`890`
- 截取字符串的全部字符：`1234567890`
- 截取字符串的第七个字符到结尾：`7890`
- 截取字符串的第一位到倒数第三位之间的字符：`234567`
- 截取字符串的第三个字符：`3`
- 截取字符串的倒数第一个字符：`0`
- 截取与原字符串顺序相反的字符串：`0987654321`
- 截取字符串倒数第三位与倒数第一位之间的字符：`89`
- 截取字符串的第一位字符到最后一位字符之间的字符，每隔一个字符截取一次：`2468`

**参考答案**

```python
str1 = '1234567890'
# - 截取字符串的第一位到第三位的字符：`123`
str2 = str1[0:4:1]
print(str2)
# - 截取字符串最后三位的字符：`890`
# - 截取字符串的全部字符：`1234567890`
# - 截取字符串的第七个字符到结尾：`7890`
# - 截取字符串的第一位到倒数第三位之间的字符：`234567`
# - 截取字符串的第三个字符：`3`
# - 截取字符串的倒数第一个字符：`0`
# - 截取与原字符串顺序相反的字符串：`0987654321`
# - 截取字符串倒数第三位与倒数第一位之间的字符：`89`
# - 截取字符串的第一位字符到最后一位字符之间的字符，每隔一个字符截取一次：`2468`
```

### 4. 设计一个程序

- 现有：`typle1 = ("tom","kaisa","alisi","xiaoming","songshu")` 我想获得“alisi”这个内容

**参考答案**

```python

```
