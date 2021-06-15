username = '숮이  💄💅👡👠🎀👙🌂👗🌂🎀💋💌'
username2 = '💄💅👡👠🎀👙🌂👗🌂🎀💋💌'
encode_username = username2.encode('utf-8')
print(encode_username)
decode_username = encode_username.decode('utf-8')
print(len(encode_username))
"""Mysql Varchar 데이터 타입의 최대 크기는 255이다."""