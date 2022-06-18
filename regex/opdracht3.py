# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Educloud web address is: educloud.global, educloud.global/info"

#Some solutions to the assingment
my_regex1 = "\w+\.\w+\/?\w+" #match all alphnum chars preceding a dot and optional has a "/", 
result1 = re.findall(my_regex1,target_string)
my_regex2 = "[a-z]+\.[a-z]+/?[a-z]+" #match all alphnum chars preceding a dot and optional has a "/", 
result2 = re.findall(my_regex2,target_string)
my_regex3 = "(?:\w+\.\w+)(?:\/?\w+)" # doing it the hard way - used non-capturing groups, 
result3 = re.findall(my_regex1,target_string) 
print(result1)
print(result2)
print(result3)