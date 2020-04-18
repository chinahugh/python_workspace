# -*- coding:utf-8 -*-


class P(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def __str__(self):
        # return self.name+" "+str(self.age)
        return 'name:%s  age:%d' % (self.name, self.age)
        # pass

if __name__ == "__main__":
    a = P("a", 1)
    b = P("b", 2)
    c = P("c", 3)
    d = P("d", 4)
    e = P("e", 5)
    list = [a, b, c, d, e]
    # list = []
    # list.append(a)
    # del list[1]
    # list.remove(list[1])
    list.reverse()
    # list.insert(1, 2)
    # print(list[-1::-1])
    print(len(list))
    for i in list:
        print(i)
        pass
    pass
pass

# ---------------------------------------------------
