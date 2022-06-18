# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Welcome Sir, how are You today?"

#Some solutions to the assingment
my_regex1 = "\\b[A-Z][a-z]+" # wordboundary for caps. followed by one or more small letters. Opposite of opdracht5
result1 = re.findall(my_regex1,target_string) 
print(result1)