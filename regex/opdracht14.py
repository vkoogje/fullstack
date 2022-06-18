# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Mijn vrienden heten Klaas, Kees en Mees"

#Some solutions to the assingment
my_regex1 = "\s" # match white spaces
result1 = re.split(my_regex1,target_string) # split on match (aka white spaces) 
print(result1)