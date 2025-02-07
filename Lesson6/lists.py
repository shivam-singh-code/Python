user = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print('Dave' in emptylist)
print(user[-2])
print(user.index('Sara'))
print(user[1:])
print(user[0:2])
print(user[0:])
print(user[-3: -1])
print(user[-3:])

print(len(user))
user.append('Elsa')
print(user)

user += ['Json']
print(user)

user.extend(['Robert', "Jimmy"])
print(user)

# user.extend(data)
# print(user)

user.insert(0, "Bob")
print(user)

user[2:2] = ["Edide", "Alex"]
print(user)

user[1:3] = ["Robert", "Jpg"]
print(user)

user.remove("Bob")
print(user)

print(user.pop())
print(user)

del user[0]
print(user)

#del data
data.clear()
print(data)


user[1:2] = ["dave"]
user.sort()
print(user)

user.sort(key=str.lower)
print(user)

num = [4, 42,81, 5]
num.reverse()
print(num)

# num.sort(reverse=True)
# print(num)

print(sorted(num, reverse=True))
print(num)

numsCopy = num.copy()
mynum = list(num)
mycopy = num[:]

print(numsCopy)
print(mycopy)
mynum.sort()
print(mynum)
print(num)

print(type(num))

mylist = list([1,'wd',True])
print(mylist)

# Tuples like list but data inside is constant and order is also constant
mytuple = tuple(('Dave', 32, True))
anothertuple = tuple((1,2,3,4))
print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(4))