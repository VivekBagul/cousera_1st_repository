# this code prints "Hello World" on console
print("Hellow World")

def multi(*args):
    ans=1
    for i in args:
        ans=ans*i
    print(ans)
    return ans
result=addition(10,20,30)