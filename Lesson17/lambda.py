squared = lambda num : num * num

print(squared(2))

addTwo = lambda num: num + 2
print(addTwo(3))

sum_total = lambda a, b: a + b
print(sum_total(2,2))

# ################################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(40))
print(addTwenty(10))

#########################################

numbers = [2,4,3,5,61,21,43]
squared_nums = map(lambda num : num * num, numbers)
print(squared_nums)
print(list(squared_nums))


######################
odd_nums = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))

##############################
from functools import reduce

numbers = [1,2,3,4,5]
total = reduce(lambda acc, curr : acc + curr, numbers, 10)
print(total)
print(sum(numbers, 10))



names = ["DAVE", "DADAEE", "WWQQWWWWWS", "WDWD DWd"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)
print(char_count)