# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Mijn vrienden heten Klaas, Kees en Mees"

#Some solutions to the assingment
my_regex1 = "[a-zA-Z]*es"
result1 = re.findall(my_regex1,target_string)
print(result1)