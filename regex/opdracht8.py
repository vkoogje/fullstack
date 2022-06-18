# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Creditcard is: 5555555555554444, 4111111111111111"

#Some solutions to the assingment
my_regex1 = "[0-9]+" # get only nums
result1 = re.findall(my_regex1,target_string)
my_regex2 = "\d+" # get only nums
result2 = re.findall(my_regex2,target_string)
my_regex3 = "[0-9]{16}" # get only nums
result3 = re.findall(my_regex3,target_string)
print(result1)
print(result2)
print(result3)