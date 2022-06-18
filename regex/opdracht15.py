# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Mijn vrienden heten Klaas, Kees en Mees"

#Some solutions to the assingment
my_regex1 = "[A-Z]" # match capital letters
match = re.finditer(my_regex1,target_string) # return a re.Match object for all matches (aka all caps) 
for result1 in match:
    print(result1.group(), result1.start(), result1.end())