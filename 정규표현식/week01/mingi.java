public class Gohome {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
	/*	1. **Matching Anything But a Newline**

		 → tester.check("...\\....\\....\\....");

		 . << 문자 한자리. \\. << .을 문자로 사용하겠다.

		3자리 . 3자리 . 3자리 . 3자리 입력마스크.

		2. **Matching Digits & Non-Digit Characters**

		→ tester.checker("\\d{2}\\D\\d{2}\\D\\d{4}"); 

		3. **Matching Specific String**

		→ tester.checker("hackerrank");

		---

		---

		1. **Matching Whitespace & Non-Whitespace Character**

		→ tester.checker("\\S{2}\\s{1}\\S{2}\\s{1}\\S{2}"); // Use \\ instead of

		/* 문자2개 공백1개

		2. **Matching Word & Non-Word Character**

		→ tester.checker("\\w{3}\\.\\w+\\.\\w{3}"); // Use \\ instead of using \

		주소3개 + . + 중간에 문자 수 개 + . 

		3. **Matching Start & End**

		→ tester.checker("^\\d{1}\\w{4}[.]{1}$"); // Use \\ instead of using \

		---

		---

		1. **Matching Specific Characters**

		→ tester.checker("^[123][120][xs0][30Aa][xsu][\\.,]$"); // Use \\

		 /* [abc]는 abc중에 있다라는 뜻.  그냥 .은 한 문자를 뜻하므로 \\. 으로 .을 문자로 쓴다는 것을 명시.

		2. **Excluding Specific Characters** 

		 → tester.checker("^[^\\d][^aeiou][^bcDF][^\\s][^AEIOU][^\\.,]$"); // Use \\ instead of using \

		3. **Matching Character Ranges**

		 → tester.checker("^[a-z][1-9][^a-z][^A-Z][A-Z].*"); // Use \\ instead of using \

		 /* ^는 문자열이 시작되었음을 알려줌 /  . * << 문자가 수 개 반복된다.
		
		*/
	}

}