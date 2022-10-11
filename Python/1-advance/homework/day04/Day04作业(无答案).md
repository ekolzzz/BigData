# Python进阶04-闭包和装饰器

[TOC]

## 能力目标

- [ ] 能够知道闭包的构成条件
- [ ] 能够知道定义闭包的语法格式
- [ ] 能够知道定义装饰器的语法格式
- [ ] 能够编写装饰器装饰带有参数和返回值的函数
- [ ] 能够写出带有参数的装饰器


## 关卡一：综合题

###  1. 闭包

题干：闭包构成的条件是什么?

**答案** ：

```

```

### 2. 装饰器

题干：什么是装饰器? 装饰器有什么特点?

**答案**：

```

```

## 关卡一：代码题

### 1. 闭包练习-01

题干：有如下代码，请问如何调用 fun_in

```python
def func_out():
    def func_in():
        print('哈哈！恭喜成功调用啦！')
    return fun_in
```

**参考答案**：

```python

```

### 2. 闭包练习-02

题干：以下是"闭包"的一个例子，你目测会打印出什么内容？

```python
def func_x():
    x = 5
    
    def func_y():
        nonlocal x
        x += 1
        return x
    
    return func_y

a = func_x()
print(a())
print(a())
print(a())
```

**参考答案**：

```

```

### 3. 装饰器练习-01

题干：一个函数, 返回一个字符串, 使用装饰器实现对这个字符串添加后缀.txt

**答案** ：

```python

```

### 4. 装饰器练习-02

题干：假设有如下两个函数：购物车添加函数、订单提交函数，要求编写一个装饰器装饰 cart 和 order 两个函数，在装饰器中模拟登录判断功能，当 username 为 'smart' 且 password 为 '123456abc' 时才调用被装饰函数，否则提示：用户未登录！

```python
def cart():
    print('购物车添加函数')
    
def order():
    print('订单提交函数')
    
# 提示用户输入用户名和密码
username = input('请输入用户名：')
password = input('请输入密码：')

cart()
order()
```

**答案** ：

```python

```

### 5. 深拷贝和浅拷贝

下面打开的打印结果为：

```python
import copy

a = [[1, 2, 3], [4, 5, 6]]
b = a
c = copy.copy(a) # 浅拷贝
d = copy.deepcopy(a) # 深拷贝

a.append(7)
a[1][2] = 0

print('原列表：', a)
print('引用赋值：', b)
print('浅拷贝：', c)
print('深拷贝：', d)
```

**答案**：

```bash
```























