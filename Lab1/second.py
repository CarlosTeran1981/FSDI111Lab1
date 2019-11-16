
print ("_" * 20)
print ("   Welcome")
print ("_" * 20)

name = input("Please type your name: ")
print(name)

age = input("Type your age: ")
# validation
ageInt = int(age)

print ("Hi, " + name)
print("You will turn," + str(ageInt + 1))

# String methods
name_length = len(name) # return length
print ("There are " + str(name_length) + " letters in your name")

print(name.upper()) # to upper
print(name.lower()) # to lower
print(name.replace ('s', 'z')) # Replace letters or words inside

print ('X' in name)