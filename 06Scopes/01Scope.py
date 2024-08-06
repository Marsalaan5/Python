username = "Mohammad Rashid"

def func():
    # username = "Arsalaan Khan"
    print(username)

print(username)
func()

# function 2

x = 99

# def func2(y):
#     z = x +  y 
#     return z 

# result = func2(1)
# print(result)


# function 3

# def func3():
#     global x 
#     x = 88

# func3()
# print(x)


# functon 4

def f1():
    x = 88 
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g= chaicoder(3)


print(f(5))
print(g(3))