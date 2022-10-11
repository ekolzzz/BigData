"""
标识符：在开发过程中，程序开发人员自己定义的一些名称（变量名、函数名、类名）
命名规则：
1）标识符由数字、字母、下划线组成，且不能以数字开头；
2）标识符区分字母的大小写；
3）标识符不能和关键字同名
    关键字：在编程语言中，一些具有特殊意义的标识符，我们自己不能使用
4）标识符应该尽量做到见名知意

常见的命名方式：
1）小驼峰命名法：标识符中第一个单词小写，后面单词的首字都大写，但是在python中不实用，在java中使用
2）大驼峰命名法：标识符中每个单词的首字母都大写，python中的类名使用
3）蛇形命名法：标识符中的每个单词都小写，单词之间以 _ 连接，python中的变量名、函数名使用
"""

# SyntaxError: invalid syntax
# 3name = 'smart'

Name = 'smart'
name = 'linda'
print(Name)
print(name)

# 查看python中有哪些关键字
import keyword
print(keyword.kwlist)

# and = 10

name = 'smart' # 见名知意【推荐】
a = 'smart' # 没有见名知意【不推荐】

# 实际开发，不要使用中文标识符
姓名 = 'linda'
print(姓名)

user_name = 'smart'


