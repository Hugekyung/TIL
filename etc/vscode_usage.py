""" VS Code: 다중 편집 단축키 """

"""
    1. Ctrl + d
    동일한 문자열에 대해 단축키를 누를 때마다 커서가 추가되어
    한꺼번에 수정할 수 있다.

    2. Ctrl + Shift + L
    동일한 문자열을 한번에 모두 선택하여
    한꺼번에 수정할 수 있다.

    3. Alt + 클릭
    클릭해 추가한 커서 위치 모두에 동시 타이핑할 수 있다.
"""

x1 = TextField(max_length=100, unique=True)
x2 = TextField(max_length=100, unique=True)
x3 = TextField(max_length=100, unique=True)
x4 = CharField(max_length=100, unique=True)
x5 = CharField(max_length=100, unique=True)

print("Alt + 클릭은 해당 커서에 동시에 타이핑할 수 있게 한다.")
print("Alt + 클릭은 해당 커서에 동시에 타이핑할 수 있게 한다.")