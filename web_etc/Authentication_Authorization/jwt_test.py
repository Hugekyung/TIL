""" JWT : Json Web Tokens 
유저가 로그인에 성공하면, Access_token의 형태로 암호화된 유저 정보를 만든다.
여기서 생성된 Access_token은 유저가 로그인헀음을(isAuthenticated) 증명하는 동시에,
Authorization에서도 활용된다.(즉, Access_token에는 유저 정보를 확인할 수 있는 정보가 담겨야 한다.)
JWT는 Authorization에서 대표적으로 활용되며, 게시물 등록 및 수정, 삭제 권한,
구독 서비스 등 다양한 서비스의 베이스가 된다."""

import jwt

SECRET = 'secret' #'랜덤한 조합의 키' 예제이므로 단순하게 'secret'이라고 하겠습니다.

access_token = jwt.encode({'id' : 1}, SECRET, algorithm = 'HS256')
print('access_token: ', access_token)

original_token = jwt.decode(access_token, SECRET, algorithms='HS256') # algorithms!! s 붙는다
print('original_token: ', original_token)