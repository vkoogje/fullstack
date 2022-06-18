# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = """Educloud addresses:
address01 = mail.educloud.com
address02 = educloud_training.com/api/def/v1/action/test01/get-token
address03 = educloud_network.com/api/gba/v02/action/testen02/get-token
address04 = educloud_platform.com/api/atc/v3/action/test03
address05 = educloud_dev.com/api/klt/v4/action/test04/get-token
address06 = educloud_dev2.com/api/nnp/v05/action/test05/get-tokens"""

# kind of cheating because of the "?<=" (positive lookbehind), which isn't in our docs.
# wel'll match on 2_=_ , 3_=_ and 5_=_ , then a whitespace and anything that comes after. 
my_regex1 = "(?<=[235]\s\=\s).+"
result1 = re.findall(my_regex1,target_string,8)

#filtering out line 2, 3, and 5 based on the ending "token"
my_regex2 = "(edu.+token$)"
result2 = re.findall(my_regex2,target_string,8)

print(result1)
print(result2)