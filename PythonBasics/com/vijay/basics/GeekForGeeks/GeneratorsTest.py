def testFunc():
    yield 11
    yield 22
    yield 44
itrVal=testFunc()
print(itrVal.__next__())# iterates for the index zero
# going to start itration from next index
for yieldVal in itrVal:
    print(yieldVal)
print(itrVal.__next__()) # trying to iterate over same iterator, signals StopIteration 
for val in testFunc():
    print(val)
    