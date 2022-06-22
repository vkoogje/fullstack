# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Welcome Sir, my web address is: educloud-training.com"

my_regex1 = "\\Bcom"
result1 = re.findall(my_regex1, target_string, 8)
print(result1)