# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Educloud email address is: info@educloud.nl, test_123@educloud.nl"

#Some solutions to the assingment
my_regex1 = "\w+@\w+\.\w+" # find all the alphnum chars befire the at sign "@", and all that follow, using an escape for the dot.
result1 = re.findall(my_regex1,target_string)

my_regex2 = "\w+@\w+\.\w+"
my_regex2_compiled = re.compile(my_regex2)
result2 = re.findall(target_string)

print(result1)
print(result2)
