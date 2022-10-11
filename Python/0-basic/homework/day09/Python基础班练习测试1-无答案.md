## Python基础班第一阶段测试题1

### 一、单选题（每题2分，共计20分：得分___）

#### 1. x 的 y 次方以下表达式正确的是?

- [ ] x^y
- [x] x**y
- [ ] x^^y
- [ ] Python 没有提到

#### 2.  `22 % 3` 表达式输出结果为？

- [ ] 7
- [x] 1
- [ ] 0
- [ ] 5

#### 3.  `4 // 3` 表达式输出结果为？

- [ ] 12
- [ ] 0
- [ ] 1.3
- [x] 1

#### 4.  以下代码的输出的结果是？

```python
if None:
    print("Hello")
```

- [ ] False
- [ ] Hello
- [x] 没有任何输出
- [ ] 语法错误

#### 5.  以下代码的输出结果?

```python
for i in [1, 0]:
    print(i+1)
```

- [x] 2

  1
- [ ] [2, 1]
- [ ] 2
- [ ] 0

#### 6. 在Python中以下那个变量是合法的？

标识符的命名规则：由下划线、字母、数字组成，不能是数字开头，不能和关键字同名

- [ ] `my#name`
- [ ] `for`
- [x] `_list`
- [ ] `2name`

#### 7. 以下代码的输出结果?

```python
i = 0
sum = 0

while i <= 4:
    sum += i
    i = i+1

print(sum)
```

- [ ] 0
- [x] 10
- [ ] 4
- [ ] 以上结果都不对

#### 8. 以下哪个描述是正确的？

- [ ] break 语句用于终止循环;
- [ ] continue 语句用于跳过当前剩余要执行的代码，执行下一次循环;
- [ ] break/continue只能用在循环中，除此以外不能单独使用;
- [x] 以上说法都是正确的;

```python
for i in range(1, 10):
	print(i)
	for j in range(1, 10):
		print(j)
		if j == 4:
			break
```

#### 9. 以下代码的输出结果?

```python
for char in 'PYTHON STRING':
  if char == ' ':
      break

  print(char, end='')
  
  if char == 'O':
      continue
```

- [x] PYTHON
- [ ] PYTHONSTRING
- [ ] PYTHN
- [ ] STRING

#### 10. 以下哪个是定义函数时的关键字？

- [ ] is
- [ ] with
- [x] def
- [ ] function

### 二、简答题（每题5分，共计20分：得分___）

#### 11. Python关键字列举5个？

```python
# 答对1个给1分
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

#### 12. 列出 Python 中的 5 种数据类型？

```python
# 答对1个给1分
int、float、bool、str、list、tuple、dict、set
```

#### 13. 列举字符串的 5 种常用方法，并分别解释有什么作用？

```python
# 答对1个给1分
my_str = 'hello python'

my_str[2:5]

my_str[:5]

my_str[6:]

my_str[::2]

my_str[::-1]
```

#### 14. 有字符串'hello python'，使用切片完成如下需求

```python
# 答对1个给1分
my_str = 'hello python'

# 需求1：截取出 'llo'
my_str[2:5]
# 需求2：截取出 'hello'
my_str[:5]
# 需求3：截取出 'python'
my_str[6:]
# 需求4：截取出 'hlopto'
my_str[::2]
# 需求5：反转字符串
my_str[::-1]
```

### 三、代码题（每题10分，共计60分：得分___）

#### 15. 计算 1~100 之间偶数的累加和（包含 1 和 100）

```python
'''代码在PyCharm写完，保证能够运行后直接拷贝到这里'''
# 方法一：
sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)

# 方法二：
list = []

for i in range(1, 101):
    if i % 2 == 0 :
        list.append(i)
print(sum(list))
```

#### 16． 字符串反转, 例如: my_str="abc" 反转后变成 "cba"

```python
'''代码在PyCharm写完，保证能够运行后直接拷贝到这里'''
my_str = "abc"

new_str = my_str[::-1]
print(new_str)
```

#### 17． 输出 100~200(包括 100 和 200)之间所有的奇数

```python
'''代码在PyCharm写完，保证能够运行后直接拷贝到这里'''
for i in range(100, 200):
    if i % 2 != 0 :
      print(i, end=',')       
```

#### 18． 使用 Python 代码实现下面图形

```python
'''
*
* *
* * *
* * * *
* * * * *
'''

i = 1
j = 1
while i <= 5:
    while j <= i:
      print('*' * j)
        j += 1
    i += 1

```

#### 19.    设计程序，打印出1-100之间除了7的倍数之外的所有数字

```python
'''代码在PyCharm写完，保证能够运行后直接拷贝到这里'''
for i in range(1, 100):
    if i % 7 != 0 :
        print(i, end=',')
```

#### 20.    猜数字游戏

> 设计一个猜数字的游戏，系统随机生成一个1~100之间的整数，玩家有5次机会，每猜一次系统就会提示玩家该数字是偏大还是偏小，如果猜中了，则告知玩家并提前结束游戏，如果5次都没猜中，结束游戏并告知正确答案。

```python
'''代码在PyCharm写完，保证能够运行后直接拷贝到这里'''
import random
print('*' * 20, '猜数字', '*' * 20)
i = int(input('请输入一个数'))
j = random.randint(1,100)

while i-5:

```

