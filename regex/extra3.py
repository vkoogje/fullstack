# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = """Dit is regel1
Dit is regel2
Dit is regel3
Dit is regel4
Dit is regel5"""


my_regex1 = "regel"
my_replace1 = "regel0"
result1 = re.sub(my_regex1, my_replace1, target_string,8)
print(result1)