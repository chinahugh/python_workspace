# import paddle.fluid as fluid

# data = fluid.layers.fill_constant(shape=[3, 4], value=16, dtype='int64')
# data = fluid.layers.Print(data, message="Print data:")

# place = fluid.CPUPlace()
# exe = fluid.Executor(place)
# exe.run(fluid.default_startup_program())

# ret = exe.run()
# ---------------------------------------------
# import paddle.fluid as fluid
# # 定义一个数据类型为int64的二维数据变量x，x第一维的维度为3，第二个维度未知，要在程序执行过程中才能确定，因此x的形状可以指定为[3, None]
# x = fluid.data(name="x", shape=[3, None], dtype="int64")
# print(x)
# # 大多数网络都会采用batch方式进行数据组织，batch大小在定义时不确定，因此batch所在维度（通常是第一维）可以指定为None
# batched_x = fluid.data(name="batched_x", shape=[None, 3, None], dtype='int64')
# print(batched_x)

# data = fluid.layers.fill_constant(shape=[3, 4], value=16, dtype='int64')
# print(data)
# ----------------------------------------------------
# import paddle.fluid as fluid

# data = fluid.layers.fill_constant(shape=[3, 4], value=16, dtype='int64')
# data = fluid.layers.Print(data, message="Print data:")

# place = fluid.CPUPlace()
# exe = fluid.Executor(place)
# exe.run(fluid.default_startup_program())

# ret = exe.run()
# ----------------------------------------------------

# 定义变量
import paddle.fluid as fluid
a = fluid.data(name="a", shape=[None, 1], dtype='int64')
b = fluid.data(name="b", shape=[None, 1], dtype='int64')

# 组建网络（此处网络仅由一个操作构成，即elementwise_add）
result = fluid.layers.elementwise_add(a,b)

# 准备运行网络
cpu = fluid.CPUPlace() # 定义运算设备，这里选择在CPU下训练
exe = fluid.Executor(cpu) # 创建执行器
exe.run(fluid.default_startup_program()) # 网络参数初始化

# 读取输入数据
import numpy
data_1 = numpy.int64(input("Please enter an integer: a="))
data_2 = numpy.int64(input("Please enter an integer: b="))
x = numpy.array([[data_1]])
y = numpy.array([[data_2]])

# 运行网络
outs = exe.run(
    feed={'a':x, 'b':y}, # 将输入数据x, y分别赋值给变量a，b
    fetch_list=[result] # 通过fetch_list参数指定需要获取的变量结果
    )

# 输出计算结果
print("%d+%d=%d" % (data_1,data_2,outs[0][0]))

outs = exe.run(
    feed={'a':x, 'b':y}, # 将输入数据x, y分别赋值给变量a，b
    fetch_list=[a,b,result] # 通过fetch_list参数指定需要获取的变量结果
    )

# 输出计算结果
print(outs)
