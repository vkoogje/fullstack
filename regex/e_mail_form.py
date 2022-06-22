# importing modules
import re       # regular expressions module

user_input1 = "my_1email-address@top1level.domain2.nl"
regex_email1 = re.compile("^\w{2,}[\.-]?\w*@\w{2,}[\.-]?\w+\.\w{2,3}$")
result1 = regex_email1.findall(user_input1)
print(result1)
if result1:
    print("email valid")
else:
    print("email not valid")