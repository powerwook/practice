# 2월 28일
#1. **Matching Specific String**
Regex_Pattern = r'hackerrank'

#2. **Matching Anything But a Newline**
""" ^로 시작점 작성후
 임의의 1자리(.) * 3 + (. + 임의의 3자리(. * 3)) * 3
 $로 종료점 작성하여 xxx.xxx.xxx.xxx 형태 유지
"""
regex_pattern = r"^.{3}(\..{3}){3}$"

#3. **Matching Digits & Non-Digit Characters**
"""
xxXxxXxxxx
x = 숫자
X = 숫자가 아닌 것 이므로
(xxX) * 2 + x * 4
"""
Regex_Pattern = r"(\d\d\D){2}\d{4}"

# 3월 1일
#1. **Matching Whitespace & Non-Whitespace Character**
"""
XXxXXxXX
x = 공백문자
X = 공백문자가 아닌 것 이므로
X * 2 + (xXX) * 2
"""
Regex_Pattern = r"\S{2}(\s\S\S){2}"

#2. **Matching Word & Non-Word Character**
"""
xxxXxxxxxxxxxxXxXxXx
x = 알파벳 + 숫자 + _ 중 하나
X = x 아닌 것
"""
Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"

#3. **Matching Start & End**
"""
^는 시작, $는 끝
xyyyy
x = 숫자
y = 알파벳 + 숫자 + _ 중 하나
"""
Regex_Pattern = r"^\d\w{4}\.$"

# 3월 2일
#1. **Matching Specific Characters**
Regex_Pattern = r'^[123][120][xs0][30Aa][xsu][.,]$'
#2. **Excluding Specific Characters**
Regex_Pattern = r'^[^0-9][^aeiou][^bcDF]\S[^AEIOU][^.,]$'
#3. **Matching Character Ranges**
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'

# 3월 3일
#1. **Matching Word Boundaries**
Regex_Pattern = r'\b[aeiouAEIOU][a-zA-Z]*\b'
#2. **Capturing & Non-Capturing Groups**
Regex_Pattern = r'(ok){3,}'	
#3. **Alternative Matching**
Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-zA-Z]+$'

# 3월 4일
#1. **Matching {x} Repetitions**
Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
#2. **Matching {x, y} Repetitions**
Regex_Pattern = r'^\w{1,2}[a-zA-Z]{3,}\W{,3}$'
#3. **Matching Zero Or More Repetitions**
Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'
#4. **Matching One Or More Repetitions**
Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'
#5. **Matching Ending Items**
Regex_Pattern = r'^[a-zA-Z]*s$'