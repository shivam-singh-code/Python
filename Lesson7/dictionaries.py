#Dictionaries

band = {
    "vocal":"plant",
    "guiter":"Page"
}

band2 = dict(vocal="plant", guiter="page")
print(band)
print(band2)
print(type(band))
print(type(band2))
print(len(band))

# Acess items
print(band["vocal"])
print(band.get("guiter"))

#list all keys
print(band.keys())

#list all values
print(band.values())

# list of key/value pair as tuples
print(band.items())

#verify a key exists
print("guiter" in band)
print("triangle" in band)

#Changes values
band["vocal"] = "Coverdale"
band.update({"bass": "Jpg"})
print(band)


#remove items
print(band.pop("bass"))
print(band)

band["drum"] = "Bonham"
print(band)

print(band.popitem()) #tuple
print(band)

# Delete and clear
band["drum"] = "Boham"
del band["drum"]
print(band)

band2.clear()
print(band2)
del band2
# print(band2)


# Copy dictonaries

# band2 = band # creates a reference
# print("bad copy")
# print(band2)
# print(band)

# band2["drums"] = "DAVE"
# print(band)

band2 = band.copy()
band2["drums"] = "DAVE"
print("Good copy!")
print(band)
print(band2)


# or use the dicitionary constructor function
band3 = dict(band)
print("!Good copy")
print(band3)

# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "Vocal"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}

band = {
    "member1": member1,
    "member2":member2
}

print(band)
print(band["member1"]["name"])

# Sets
nums = {1,2,3,4}
nums2 = set({1,2,3,4})
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicates allowed 
nums = {1,2,2,3}
print(nums)
print(len(nums))

# True is a dupe of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or key

# Add new element to a set
nums.add(8)
print(nums)

# Add elements form one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

# You can use update with lists, tuples, and dictionaries, too

# Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

# keep everything excepts the duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)