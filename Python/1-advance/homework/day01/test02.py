"""
- 定义一个Star类(明星类)， 通过明星类创建一个zhou_xing_chi对象

  使用__init__方法给对象添加属性

  print打印对象时输出"xxx是我的偶像，我非常喜欢他的电影yyy"

  xxx为明星姓名，yyy是电影的名字
"""

"""
明星类：

1）属性
_name：哪个明星
_film：哪部电影
# _judge：评价【好看】【非常好看】【难看】【非常难看】

2）方法
__init__：属性初始化
playing：打印"xxx是我的偶像，我非常喜欢他的电影yyy"

"""


class Star(object):
    def __init__(self, _name, _film):
        self.name = _name
        self.film = _film
        # self.judge = _judge


    def playing(self):
        print(f'{self.name}是我的偶像，我非常喜欢他的电影{self.film}')

zhou_xing_chi = Star('周星驰','《大话西游》')
zhou_xing_chi.playing()

lu_han = Star('鹿晗','《上海堡垒》')
lu_han.playing()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      