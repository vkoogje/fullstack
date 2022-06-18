# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Creditcard is: 1115695236754643, 2229235862247776,3338231899282236,4441131212281851"

my_regex1 = "[13]\d{13}"
result1 = re.findall(my_regex1, target_string, 8)
print(result1)