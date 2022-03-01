#1. Matching Specific String
import re
Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

#2. Matching Digits & Non-Digit Characters
# \.이것은 점을 의미함 $은 문자열 종료?를 말하는걸로 알고있음.
import re
regex_pattern = r"...\....\....\....$"	# Do not delete 'r'.

#3.Matching Anything But a Newline
# 문제에서 x는 숫자,X는 문자라고했으니까
import re
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.


#4. Matching Whitespace & Non-Whitespace Character
import re
Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.
# 문제에서 \s:any whitespace character
#         \S:any non-whitespace character

#5. Matching Word & Non-Word Character
import re
Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"	# Do not delete 'r'.

#6. Matching Start & End
import re
Regex_Pattern = r"^[0-9]\w\w\w\w\.$"	# Do not delete 'r'.
#문제조건1:숫자시작이므로 ^[0-9]
#문제조건2:x가 word character이므로 \w\w\w\w
#문제조건3:.으로 끝나야함 따라서 \.$를 해줬음.
