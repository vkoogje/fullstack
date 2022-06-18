# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = """Dit is dummy tekst.
En dit is de tweede regel.
En dit is de derde regel.
En dit is de vierde regel Password:12abc!$.
En dit is de vijfde regel"""

my_regex1 = "(Password:)([a-zA-Z0-9!$]{6,10})"
my_replace1 = "Password:****"
result1 = re.sub(my_regex1, my_replace1, target_string)
print(result1)