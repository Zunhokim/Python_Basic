'''
사이트별로 비밀번호를 만들어주는 프로그램 작성. 

예) http://naver.com
Rule 1 : http:// 부분은 제외 >> naver.com
Rule 2 : 처음 나오는 점(.) 이후 부분은 제외 >> naver
Rule 3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + "!"로 구성

예) 생성된 비밀번호 : nav51!
'''

site = "http://naver.com"
sol1 = site.replace("http://", "")
passkey = sol1[:sol1.index(".")]

print("Password : "+ passkey[:3] + str(len(passkey)) + str(passkey.count("e")) + "!")