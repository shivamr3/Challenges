def func(objVar, key):
    keyList = key.split("/")
    tempVar = objVar
    for key in keyList:
        if tempVar.get(key):
            tempVar = tempVar[key]
        else:
            return None
    return tempVar

objVar = {"x":{"y":{"z":"a"}}}
objVal = func(objVar,"x/y/z")
print("Value one = ", objVal)

objVar1 = {"a":{"b":{"c":"d"}}}
objVal1 = func(objVar1,"a/b/c")
print("Value two = ", objVal1)