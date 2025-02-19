import os
# r = Read
# a = append
# w = write
# x = create
# rawx

# Read - error if it does't exist

f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("File does not exists!")
finally:
    f.close()

# Append - created the file if it doesn't exist
f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()


# Write(overwrite)
f = open("context.txt", "w")
f.write("I deleted all of context")
f.close()

f= open("context.txt")
print(f.read())
f.close()


# Two ways to create a new file

# Opens a file for writing, create the file if it does not exists
f = open("name_list.txt", "w")
f.close()

# Create the specified file but return an error if the file exists
if not os.path.exists('dave.txt'):
    f = open('dave.txt',"x")
    f.close()

# Delete a file
    
# avoid an error if it does't exist
if os.path.exists("dave.txt"):
    os.remove('dave.txt')
else:
    print("The file you wish to delete does not exist")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)