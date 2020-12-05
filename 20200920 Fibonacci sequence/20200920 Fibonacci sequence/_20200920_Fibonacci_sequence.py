def f1():
    print(x)
def f2():
    global x
    x=50
    print(x)
x=10
f2()
f1()