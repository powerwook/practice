1.Regex_Pattern = r'hackerrank'

2.Regex_pattern = r"...\....\....\....$"

3.Regex_Pattern = r"\d\d.\d\d.\d\d\d\d"

# 1. Matching Whitespace & Non-Whitespace Character
Regex_Pattern = r"\S{2}(\s\S\S){2}"	# Do not delete 'r'.

#2. Matching Anything But a Newline
Regex_Pattern = r"\w{3}\W(\w){10}\W\w{3}"	

#3. Matching Start & End
Regex_Pattern = r"^\d\w{4}\.$"