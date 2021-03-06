# importing modules
import re       # regular expressions module

# string we want to match our expressions on
target_string = "Educloud phone number is: 06-123-456 and 06.123.456"

#Some solutions to the assingment
my_regex1 = "\d+\D?\d+\D?\d+" #matching against 1 or more digits in a row, followed by zero or one non-digit. And repeat this.
result1 = re.findall(my_regex1,target_string)
my_regex2 = "\d{2}.-?\d{3}.-?\d{3}" # matching against 2 digits and zero or more non-digits. Then the same but with 3 digits and repeat
result2 = re.findall(my_regex2,target_string)
my_regex3 = "\d{2}[.-]?\d{3}[.-]?\d{3}" # same as 2, but with ranges for the non-digits
result3 = re.findall(my_regex3,target_string)
my_regex4 = "[0-9]{2}[.-]?[0-9]{3}[.-]?[0-9]{3}" # using ranging, and quantifiers to filter out the phone number, same principle as my_regex2/3
result4 = re.findall(my_regex4,target_string)
my_regex5 = "\d+.\d+.\d+"
result5 =re.findall(my_regex5,target_string)
my_regex6 = "\d+.\d+.\d+"
my_regex6_compiled = re.compile(my_regex6)
result6 = my_regex6_compiled.findall(target_string)


print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)