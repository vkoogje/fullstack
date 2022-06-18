# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Numbers: 1 2 3 4 5 6 7 8 9 10"

#Some solutions to the assingment
my_regex1 = "[5-8]"
result1 = re.findall(my_regex1,target_string)
print(result1)