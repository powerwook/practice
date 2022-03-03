
#1. Matching Specific String
Regex_Pattern =  r'a-zA-Z'	# Do not delete 'r'.
import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))


#2. Matching Anything But a Newline


regex_pattern = r"^...\....\....\....$"	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())


#3. Matching Digits & Non-Digit Characters

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())


#4.Matching Whitespace & Non-Whitespace Character

Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower()) 



#5. Matching Word & Non-Word Character


Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())


#6. Matching Start & End
Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
