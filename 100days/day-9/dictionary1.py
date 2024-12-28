programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }

programming_dictionary["Bug"]

# Add new items to dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary["Loop"])

empty_dictionary = {}

# programming_dictionary = {}
# print(programming_dictionary)

programming_dictionary["Bug"] = "This is my newest entry text"
print(programming_dictionary["Bug"])

#loop through a dictionary with for statement
for thing in programming_dictionary:
    print(programming_dictionary[thing])