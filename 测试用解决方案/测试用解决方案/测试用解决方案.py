import math
class Circle:
    def __init__(self,r=0):
        self.__radius=r
    def __del__(self):
        print("运行析构函数中")
    def SetRadius(self):
        self.__radius=eval(input("半径："))
    def Area(self):
        return self.__radius**2*math.pi
    def Perometer(self):
        return self.__radius*2*math.pi
if __name__=='__main__':
    cir1=Circle(3)
    print("cir1的面积为：%s"%cir1.Area())
    print("cir1的周长为：%s"%cir1.Perometer())
    cir2=Circle()
    cir2.SetRadius()
    print("cir2的面积为：%s"%cir2.Area())
    print("cir2的周长为：%s"%cir2.Perometer())
    cir1.__del__()
    cir2.__del__()