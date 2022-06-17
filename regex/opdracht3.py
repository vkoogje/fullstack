# importing modules
import re           # regular expressions module


target_string = "Educloud web address is: educloud.global, educloud.global/info"

my_regex1 = "\w+\.\w+/?\w+" #match all alphnum chars preceding a dot and optional has a "/", 
result1 = re.findall(my_regex1,target_string)
print(result1)
