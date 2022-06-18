# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Educloud phone number is: 06-123-456 and 0800-123-456"

#Some solutions to the assingment
my_regex1 = "\\b[0-6]{2}\D\d+\D\d+" # binding [0-6], then look for non-diget. Can't use only [0-9], if we do the 00 of 0800 will also show up.
result1 = re.findall(my_regex1,target_string)
my_regex2 = "\\b[0-6]{2}.[0-9]+.[0-9+]+" # same priciple as my_regex1
result2 = re.findall(my_regex2,target_string)
my_regex3 = "06.[0-9]+.[0-9+]+" # filter 06, and then the rest.
result3 = re.findall(my_regex3,target_string)
my_regex4 = "0[68]0*.\d+.\d+"
result4 = re.findall(my_regex4,target_string)
print(result1)
print(result2)
print(result3)
print(result4)