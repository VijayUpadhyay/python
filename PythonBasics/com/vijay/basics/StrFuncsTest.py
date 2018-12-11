str1 = "vijay upadhyaya"
print(str1.capitalize())
print(str1.title())
print(str1.center(30, "*"))
print(str1.count('ay'))
print(str1.endswith("aya"))
print(str1.endswith("ay"))
Str = 'this is string example....wow!!!'
suffix = '!!'
suffix2 = "test2"
print (Str.endswith(suffix))
print (Str.endswith(suffix, 10))
print (Str.endswith(suffix, 5, 8))
str2 = "this is\tstring example....wow!!!"
print ("Original string: %s" % (str2))
print ("Default exapanded tab: " + str2.expandtabs())
print ("Double exapanded tab: " + str2.expandtabs(16))
print ("Double exapanded tab: " + str2.expandtabs(1))
print ("Double exapanded tab: " + str2.expandtabs(-1))
print("===========================")
print("is alphanumeric:", str1.isalnum())
print("is alphanumeric:", suffix2.isalnum())
print("zfill", str1.zfill(50))
print("upper::", str1.upper())