# importing modules
import re           # regular expressions module

target_string = "Educloud email address is: info@educloud.nl, test_123@educloud.nl"

my_regex1 = "\w+@\w+\.\w+" # find all the alphnum chars befire the at sign "@", and all that follow, using an escape for the dot.
result1 = re.findall(my_regex1,target_string)
print(result1)