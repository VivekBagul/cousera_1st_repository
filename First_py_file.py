# this code prints "Hello World" on console
print("Hellow World")
def addition(*args):
    ans=0
    for i in args:
        ans=ans+i
    print(ans)
    return ans
result=addition(10,20,30)
print("func completed")
