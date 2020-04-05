## !/usr/bin/python3

# if True:
#     print ("Answer")
#     print ("True")
# else:
#     print ("Answer")
#     print ("False")    # 缩进不一致，会导致运行错误
# # ---------------------

 
# str='Runoob'
 
# print(str)                 # 输出字符串
# print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
# print(str[0])              # 输出字符串第一个字符
# print(str[2:5])            # 输出从第三个开始到第五个的字符
# print(str[2:])             # 输出从第三个开始后的所有字符
# print(str * 2)             # 输出字符串两次
# print(str + '你好')        # 连接字符串
 
# print('------------------------------')
 
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# ------------
# a = 111
# print(isinstance(a, int))
 
#  ------------------

# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# print(list)
# ---------------------------------
# def reverseWords(input):
     
#     # 通过空格将字符串分隔符，把各个单词分隔为列表
#     inputWords = input.split(" ")
 
#     # 翻转字符串
#     # 假设列表 list = [1,2,3,4],  
#     # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
#     # inputWords[-1::-1] 有三个参数
#     # 第一个参数 -1 表示最后一个元素
#     # 第二个参数为空，表示移动到列表末尾
#     # 第三个参数为步长，-1 表示逆向
#     inputWords=inputWords[-1::-1]
 
#     # 重新组合字符串
#     output = ' '.join(inputWords)
     
#     return output
 
# if __name__ == "__main__":
#     input = 'I like runoob'
#     print(input)
#     rw = reverseWords(input)
#     print(rw)
# ---------------
# 在 Python 3.8中
# x=1
# print(f'{x+1=}')

# ---------------------
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 10:
#     print(b)
#     # a, b = b, a+b
#     b,a = a+b,b

# count = 0
# while count < 5:
#    print (count, " 小于 5")
#    count = count + 1
# else:
#    print (count, " 大于或等于 5")
# import sys
# print(sys.path)
# print(dir(sys))
# 打开一个文件
# f = open("foo.txt", "w",encoding='utf-8')

# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# # 关闭打开的文件
# f.close()

# import sys
# print( sys.getdefaultencoding())

# ------------------
# f = open("foo.txt", "r",encoding='utf-8')
# str = f.read()
# print(str)

# # 关闭打开的文件
# f.close()

# 打开一个文件
f = open("study/foo.txt", "r",encoding='utf-8')

# str = f.readline()
print(str)
ls=f.readlines()
print(ls)

# 关闭打开的文件
f.close()
# ----------------------------------
# a = 10
# b = 20
# if ( a and b ):
#        print ("1 - 变量 a 和 b 都为 true")
# else:
#    print ("1 - 变量 a 和 b 有一个不为 true")
 
# if ( a or b ):
#    print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#    print ("2 - 变量 a 和 b 都不为 true")
# # 修改变量 a 的值
# a = 0
# if ( a and b ):
#    print ("3 - 变量 a 和 b 都为 true")
# else:
#    print ("3 - 变量 a 和 b 有一个不为 true")
 
# if ( a or b ):
#    print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#    print ("4 - 变量 a 和 b 都不为 true")
 
# if not( a and b ):
#    print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
# else:
#    print ("5 - 变量 a 和 b 都为 true")