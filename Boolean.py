class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))  

def myfunc():
    return True
print(myfunc())

def myFunction():
    return True
if myFunction():
    print("YES!")

else:
    print("NO!")

x = 200
print(isinstance(x, int))

print(10 > 9)
print(10 == 9)
print(10 < 9)

