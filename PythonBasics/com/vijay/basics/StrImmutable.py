var1 = "vijay"
var2 = var1
print("var1 ref: ", id(var1))
print("var2 ref: ", id(var2))
print("equals check 0: ", var1 == var2)
var1 = "rakesh"
print("equals check 1: ", var1 == var2)
var3 = "rakesh"
print("equals check 2: ", var1 == var3)
dataType = type(var1)
print("var3 ref: ", id(var3))
print("data type is: ", dataType)
var1 = var1 + "test"  # changing value changes the object. created new object with same name.
print("equals check 3: ", var1 == var3)
# reference test
print(id(var1))
print(id(var3))
