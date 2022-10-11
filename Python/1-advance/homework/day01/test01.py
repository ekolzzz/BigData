"""
- 定义一个Star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

  使用\__init__方法给对象添加属性

  定义方法playing()，打印“xxx出演了yyy，非常好看”
  """
"""
面向对象思维分析：
1) 分解对象: 根据要解决的问题,分析问题中涉及到哪些对象
    
2) 抽象出类: 分解出每个对象抽象成一个类，分析类的对象有哪些属性和方法
    
3) 定义类: 根据2) 来定义类

4) 通过类创建对象,实现功能

明星类：
1）属性
    _name：哪个明星
    _film：哪部电影
    _judge：评价【好看】【非常好看】【难看】【非常难看】

2）方法
    __init__：属性初始化
    playing：打印“xxx出演了yyy，非常好看”
    
"""

class Star(object):
    def __init__(self, _name, _film, _judge):
        self.name = _name
        self.film = _film
        self.judge = _judge


    def playing(self):
        print(f'{self.name}出演了{self.film}，{self.judge}')

zhou_xing_chi = Star('周星驰','大话西游','非常好看')
zhou_xing_chi.playing()

lu_han = Star('鹿晗','上海堡垒','非常难看')
lu_han.playing()



