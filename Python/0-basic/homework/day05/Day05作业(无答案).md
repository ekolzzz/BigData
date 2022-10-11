# Python基础05-容器类型、函数

[TOC]

## 能力目标

- [ ] 能够说出函数定义的语法格式
- [ ] 能够说出函数调用的语法格式
- [ ] 知道return关键字可以使函数返回一个结果
- [ ] 能说出局部变量的特点(定义方式，作用范围)
- [ ] 能说出全局变量的特点(定义方式，作用范围)



## 关卡一：基础题

### 1. 函数是什么，函数的作用，函数怎么使用？

**参考答案**

```python
函数：是把具有独立功能的代码块组织为一个整体；

函数的作用：在开发程序时，使用函数可以提高编写的效率以及代码的 重用

函数的使用：
			1.定义函数 —— 在函数中编写代码，实现功能
			2.调用函数 —— 执行编写的代码
```

### 2. 定义、调用函数的格式分别是什么？

**参考答案**

```python
# 定义格式
def 函数名():
  函数体
  
# 调用格式
函数名()
```

### 3. 函数中形参和实参分别是什么？

**参考答案**

```python
形参：定义函数时设置的参数，是用来 代替真实数据 的，在函数内部 作为变量使用
实参：调用函数时设置的 真实数据，会被传递到 函数内部
```

### 4. 函数中如何设置返回值？如果不设置返回值，函数默认会返回什么？

**参考答案**

```python
在函数中使用 return 关键字可以返回结果
不设置返回值, 会返回None, 表示没有任何数据
```

### 5.什么是局部变量？什么是全局变量？

**参考答案**

```python
局部变量，就是在 函数内部定义的变量
局部变量的作用域只在函数内部

在函数外边定义的变量叫做 全局变量
全局变量能够在所有的函数中进行访问
```

### 6.函数内部如何修改全局变量？

**参考答案**

```python
函数内赋值变量时，默认为定义并赋值局部变量

如果在函数中修改全局变量，那么就需要使用global进行声明
```


## 关卡二：综合题

### 1. 设计一个程序

- 将下列两个列表合并，将合并后的列表去重，之后降序并输出

  list1 = [11, 45, 34, 51, 90]
  list2 = [4, 16, 23, 0]

**参考答案**

```python
list1 = [11, 45, 34, 51, 90]
list2 = [4, 16, 23, 0]

list = list(set(list1 + list2))

# 升序
# list.sort()

# 降序
# list.sort(reverse= True)
list.reverse()

print(list)
```



### 2. 设计一个程序

- 定义一个函数max，接受的参数类型是数值，最终返回两个数中的最大值

**参考答案**

```python
def max(a, b) :
    if a > b :
        max = a
    else:
        max = b
    return max

a = int(input('请输入一个数：'))
b = int(input('请输入另一个数：'))

print(max(a, b))
```



### 3. 设计一个程序:

- 用函数实现一个判断用户输入的年份是否是闰年的程序，在函数中打印结果。

    ##### 训练提示

    1. 能被400整除的年份
    2. 能被4整除，但是不能被100整除的年份，以上2种方法满足一种即为闰年

**参考答案**

```python
while True :
    print('============闰年查询器============')
    year = int(input('请输入要查询的年份：'))

    def leap_year(year) :
        if year % 4 == 0 and year % 100 != 0 :
            print(year, '是闰年')

        else:
            print(year, '不是闰年')

    leap_year(year)
    continue
```



### 4. 设计一个程序:

- 定义一个函数，计算两个数之和。调用者在得到结果的时候需要判断是否大于20，如果大于则输出，超过10的加法太难了

**参考答案**

```python
def sum(num1, num2):
  """计算两数之和"""
  sum = num1 + num2
  return sum

num1 = int(input('请输入一个数：'))
num2 = int(input('请输入另一个数：'))

my_sum = sum(num1, num2)

print()
if my_sum <= 10:
  print('%d+%d=%d' % (num1, num2, my_sum))
else:
  print('超过10的加法太难了')
```


### 5. 设计一个程序:

* 完成一个函数，给定三个值。判断你给的值是否可以组成一个三角形

训练提示：

  三角形成立必须两边之和大于第三边

  第一步：定义函数，并接受三个参数

  第二步：任意相加其中的两条边判断是否大于第三边，要保证三条边中任意两边之和都大于第三边

**参考答案**

```python
def my_fun(list, a, b, c):
    if a+b > c:
        print(list, '可以组成三角形')
    else:
        print(list, '不可以组成三角形')

while True :
    print('==============三角形判断器==============')

    i = 1
    list = []

    while i <= 3 :
        list.append(int(input('请输入第%d个数：' % i)))
        i +=1

    list.sort() # 升序，确定大小：list[0]<list[1]<list[2]

    my_fun(list,list[0],list[1],list[2])
    
```


## 关卡三：扩展题

### 1. 设计一个程序:

- 定义一个函数，接受三个参数，分别为字符串s、数值a1、数值a2，将字符串s从下标a1开始的a2个字符删除，并把结果返回

  ##### 训练提示

  ​	1、函数的定义

  ​	2、函数的参数

  ​	3、字符串的切割

例如：

```
s = "123456789", a1 = 2, a2 = 4 结果为: "12789"
```

**参考答案**

``` python
def my_task(str, a1, a2):
    str1 = str[:a1+1]
    str2 = str[a1+a2-1:] 
    return str1 + str2

str = input('请输入一个字符串：')
a1 = int(input('请输入数值1：'))
a2 = int(input('请输入数值2：'))

print(my_task(str, a1, a2))
```

### 2. 设计一个程序:

定义一个函数

- 接收参数 num 和 command
- command 为 True 则返回0-n(包含n)以内的偶数组成的列表
- command 为 False 则返回0-n(包含n)以内的奇数组成的列表

```python
# def my_task(num, com):
#     i = 0
#     even_list = []
#     odd_list = []
#      #如果命令为True,则输出偶数
#     while i <= num :
#         if i % 2 == 0 :
#             even_list.append(i) # 偶数列表
#         else:
#             odd_list.append(i) # 奇数列表
#         i += 1
# 
#     if com == 'True':
#         # print(even_list)
#         return (even_list)
# 
#     else:
#         # print(odd_list)
#         return (odd_list)
# 
# while True :
#     num= int(input('请输入num:'))
#     com= input('请输入command:')
# 
#     print(my_task(num, com))
```

**提示：**

- 函数里创建一个空列表，遍历0-num的数字，每当有一个奇数/偶数就添加到列表，最终返回列表

  