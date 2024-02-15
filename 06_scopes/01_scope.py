username = "Harshvardhan"

def func():
    username = "DP"
    print(username)

print(username)
func()

x = 58

def func2(y):
    z = x + y
    return z

result = func2(22)
print(result)

def func3():
    global x
    x = 88
    print(x)

func3()
print(x)

def f1():
    # x = 22
    def f2():
        print(x)
    f2()

f1()

def f3():
    x = 22
    def f4():
        print(x)
    return f4

my_result = f3()
my_result()

def love_coder(num):
    def actual(x):
        return x ** num
    return actual

demo = love_coder(2)
resulting = demo(5)
print(resulting)

