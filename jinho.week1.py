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

#7.Matching Specific Characters
import re
Regex_Pattern = r'^[1|2|3][1|2|0][0|s|x][0|3|a|A][s|u|x][.|,]'
#or연산(|)하고 ^문자열시작이 핵심임

#8.Excluding Specific Characters
import re
Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIOU][^.,]$'	# Do not delete 'r'.
#\D는 숫자가 아닌 것과 매치된다.


#9.Matching Character Ranges
import re
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'	# Do not delete 'r'.
# ^는 []안에서쓰이지않으면 문자열시작을 알리는것이 핵심이다.

