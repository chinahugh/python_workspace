# -*- coding: utf-8 -*-
class MyClass(object):
    """一个简单的类实例"""
    __i = 12345
    def f(self):
        return 'hello world'
    def __init__(self,a):
        self.data=[]
        self.__a=a
        print(self)

    @property 
    def __geta(self):
       return self.__a
    @classmethod
    def classdef(cls):
       return MyClass.__i


 
# 实例化类
if __name__ == "__main__":
   x = MyClass(9)
   print("MyClass 类 x 为：", x)
   print("MyClass 类 x.__dict__ 为：", x.__dict__)
   print("MyClass 类 x.dir 为：", dir(x))
   # 访问类的属性和方法
   print("MyClass 类的属性 i 为：", x._MyClass__i)
   print("MyClass 类的方法 f 输出为：", x.f())
   print(x._MyClass__geta)
   print(MyClass.classdef())


# ------------------------------------------------------

#类定义
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
#单继承示例
# class student(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         #调用父类的构函
#         people.__init__(self,n,a,w)
#         self.grade = g
#     #覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
 
 
# s = student('ken',10,60,3)
# s.speak()
# super(student,s).speak()   #调用父类方法

# -----------------------

#类定义
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
#         print(self.__weight)
 
# # 实例化类
# p = people('runoob',10,30)
# p.speak()
# # -----------------
# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b
 
#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
   
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)
 
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print (v1 + v2)
# --------------------------------------

# if True:
#     msg="asdasd"
# print(msg)

# ---------------------------

# def outer():
#     num = 10
#     def inner():
#        # nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()
# --------------------
# import os
# os.chdir('D:\\')   # 修改当前的工作目录
# os.system('mkdir today')   # 执行系统命令 mkdir 
# ----------------
