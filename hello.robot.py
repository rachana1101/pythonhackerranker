print("hello world")
#just playing with python 

myString = "kemo"
myInt = 1 
myboolean = False
myList = [1, 2, 3]
myDictionary = {"one":1, "two": 2, "three": 3}
mySet = {1, 3, 3}

print (mySet)

myFloat = 3.2 
myInt = int (myFloat)

print(myInt)

# number manipulation 
myNumber = 3.2434
print ("numbers", myNumber)
print ("num %d" %(myNumber))
print ("num %.2f" %(myNumber))
print(f"my nums are {myNumber} and {myFloat}")

# string print 
nameString = "my name is Rachana and I am not a robot"
print(nameString[0:5])
print(nameString[4:10])
print(nameString[:8])
print(nameString[8:])

# string manipulation 
valueString = "keno and rachana are made for each other"
print(valueString.split())
print(valueString.splitlines())
print(valueString.count("keno"))

# list manipulation 
stringList = ["rachana", "keno"]
intList = [1,2,3]
mixedList = ['rachana', 1, 4, 'keno']
listOfList = [[1,2,3], [2,4,6]]

debug = 1 

print(mixedList[0:10])
print(mixedList[0])
print(mixedList[-1])
print(mixedList[0::2])
print(mixedList.append("rrr"))
print(mixedList)

print(intList.sort())

#tuple demo 
myTuple = (1,2,3,4,5,6,1)

print(myTuple)
print(myTuple[0])
print(myTuple[0:2])
print(myTuple.count(1))

#set demo 
#dictionary demo 

myMap = {"one": 1, "two": 2, "three": 3}
print(myMap)
print(myMap.keys())
print(myMap.values())
print(myMap["one"])

myMap["one"] = 11
print(myMap)







