"""
函数实参传递的 2 种方式：
1）位置实参：传递实参时，不需要指定形参的名称，而是按照形参的顺序来传递实参。比如：func(1, 5, 3)
2）关键字实参：传递实参时，需要指定形参的名称，按照 `形参名=数据` 的形式来传递实参。比如：func(a=1, b=5, c=3)

函数形参的 4 个分类：
1）普通形参：函数调用时，必须传实参；比如：def func1(a, b, c)
2）缺省形参：形参带有默认值，函数调用时，可以传实参，也可以不传；比如：def func1(a, b=2, c=3)
3）元祖不定长形参：用于接收任意数量的位置实参；比如：def func1(*args)
4）字典不定长形参：用于接收任意数量的关键字实参；比如：def func1(**kwargs)

*args和**kwargs作为形参：
1）*args形参：元祖不定长形参，用于接收任意数量的位置实参
2）**kwargs形参：字典不定长形参，用于接收任意数量的关键字实参
"""





"""
*列表或*元祖：传递实参时，如果在列表或元祖数据前加*，表示把列表或元祖中的每个元素作为实参按位置传递给被调用函数的形参
**字典：传递实参时，如果在字典数据前加**，表示把字典中的每个key-value对作为一个关键字实参传递给被调用函数的形参，
       key相当于参数名，value相当于参数的值
"""




