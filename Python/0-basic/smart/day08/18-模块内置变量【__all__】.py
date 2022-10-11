"""
模块内置变量：__all__
学习目标：能够通过模块内置变量 __all__ 限定 `from 模块 import *` 方式默认导入的内容
"""


"""
模块内置变量：__all__

使用 `from 模块 import *` 的方式导入模块的内容时，默认只会导入被导入模块中 __all__ 内置
变量中指定的内容
"""


"""
注意：
1）在 smart.py 模块的最上方添加右边的代码：__all__ = ['num', 'sum']
2）在添加之前或添加之后，分别运行当前文件的代码查看效果

结果：
1）smart.py 中未添加 __all__ = ['num', 'sum'] 内容之前，`from smart import *` 默认
会导入 smart 模块的所有内容
2）smart.py 中添加了 __all__ = ['num', 'sum'] 内容之后，`from smart import *` 只能
导入 __all__ 中限定的内容
"""

# from 模块名 import *
# 这是的import * 其实代表的是被导入模块中 __all__ 这个内置变量限定的所有内容
from smart import *


print(num)

res = my_sum(1, 2)
print(res)


res = my_sub(3, 1)
print(res)
















