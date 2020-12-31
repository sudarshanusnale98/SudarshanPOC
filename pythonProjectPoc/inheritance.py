from numpy import *

m = array([['Mon', 18, 20, 22, 17]])


class Bus:
    def append(self):
        print("In Bus")
        m_r = append(m, [['Avg', 12, 15, 13, 11]], 0)
        return m_r


class School(Bus):
    def m(self):
        print("In School")
        print(m)


obj = School()
obj.m()
m = obj.append()
obj.m()

