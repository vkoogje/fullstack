# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Welcome Sir, how are You today?"

#Some solutions to the assingment
my_regex1 = "\\b[a-z]+" # wordboundary for small letters. If we would use [a-z] only, we'd still get for example 'elcome and 'ou'
result1 = re.findall(my_regex1,target_string)
print(result1)