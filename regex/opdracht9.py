# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Creditcard is: 5555555555554444, 4111111111111111"

#Some solutions to the assingment
my_regex1 = "\d" # we're going to replace a digit at a time, so we have to match one digit at a time. Don't need a quantifier
result1 = re.sub(my_regex1, "a", target_string)
my_regex2 = "[0-9]" # we're going to replace a digit at a time, so we have to match one digit at a time. Don't need a quantifier
result2 = re.sub(my_regex2, "a", target_string)
print(result1)
print(result2)