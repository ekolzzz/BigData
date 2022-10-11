```python
class Student(object):
    count = 0 # 记录总学生数
    boy = 0 # 记录男生数
    girl = 0 # 记录女生数
    
    def __init__(self, _name, _age, _gender):
        self.name = _name # 姓名
        self.age = _age # 年龄
        self.gender = _gender # 性别
        
        Student.count += 1
        # 假设：True表示男,False表示女
        if _gender:
            Student.boy += 1
        else:
            Student.girl += 1
        
    # 实例方法
    def show_stu_info(self):
        print(f'姓名:{self.name}，年龄:{self.age}，性别:{self.gender}')
            
    # 类方法
    @classmethod
    def show_count_info(cls):
        print(f'总学生数:{cls.count}，男生数:{cls.boy}，女生数:{cls.girl}')
```

## 面向对象day03-知识点总结

1）实例属性和类属性【理解】

**目标**：区分实例属性和类属性

* 实例属性：每个实例对象都有一份数据，互不相干，由各自的内存来保存
  * 比如：我们每个人的姓名、年龄...
* 类属性：记录一类事物共同的数据，在这个类中只有一份，这一份数据被这个类的所有实例对象共有
  * 比如：记录一共有多个人
  * 注意：无论是类属性的访问还是修改，都直接`类名`操作
    * 访问：`类名.类属性名`
    * 修改：`类名.类属性名 = 值`

2）实例方法、类方法、静态方法【理解】

**目标**：区分实例方法、类方法、静态方法

* 实例方法：需要访问每个实例对象的各自的数据

  * 调用：`实例对象.实例方法(...)`

  ```python
  def show_info(self):
      print(f'我的名字：{self.name}, 年龄：{self.age}')
  ```

* 类方法：只需要访问类属性数据，跟实例对象没关系

  * 调用：`类名.类方法(...)`

  ```python
  @classmethod
  def show_dog_count(cls):
      # print('测试cls：', id(cls))
      # print(f'现在一个有{Dog.count}只狗')
      print(f'现在一个有{cls.count}只狗')
  ```

* 静态方法：逻辑上属于类，但是不需要使用类中的任何数据（类属性、实例属性都用不到）

  * 调用：`类名.静态方法(...)`

  ```python
  class SysManager(object):
      """管理系统类"""
      # 需求：提供一个显示菜单的方法
      @staticmethod
      def show_menu():
          print('====================')
          print('= 1. 新增一个学生')
          print('= 2. 查询所有学生')
          print('= 3. 查询某个学生')
          print('= 4. 修改某个学生')
          print('= 5. 删除某个学生')
          print('= ...')
          print('====================')
  ```

3）学生名片管理系统-面向对象版【理解】

**目标**：面向对象基础语法练习、面向对象编程步骤分析

> 具体参加课堂代码

4）扩展内容【了解】

`pickle模块`：

```
* pickle.dumps(数据)：将数据转换为可以写入到文件中的一个二进制bytes数据
* pickle.loads(二进制bytes数据)：将二进制bytes数据恢复成原来的数据
```

`万物皆对象`：

* 在 python 中，所有的东西其实都是"对象"
* 无论是基本类型数据、容器类型数据、函数、类，本质上都是对象





















