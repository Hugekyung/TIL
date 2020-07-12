## git bash를 활용해 github에 file 업로드하는 방법

### 업로드 전 해두어야 하는 기본 작업

[git config(최초 1회만 실행)]

- git commit에 사용될 username 등록

```shell
$ git config --global user.name "your_name"
```

- git commit에 사용될 email 등록

```shell
$ git config --global user.email "your_email@example.com"
```

- 설정한 내용 확인하기

```shell
$ git config --list
```



[git init]

- 로컬 저장소로 설정할 프로젝트 위치로 이동하기

```shell
$ cd <폴더이름>
```

- 로컬저장소로 설정

- (master)가 나타나면, 해당 폴더는 git bash에 의해 관리되고 있다는 뜻

```shell
$ git init
```

- init 취소하기

```shell
$ rm -r.git
```



[git status]

- 로컬저장소의 현재 상태 확인하기
- 명령어가 동작하지 않을 때 에러 확인 가능

```shell
$ git status
```



## [git bash를 이용해 fold  및 file을 github에 올리는 기본적인 절차]

1. git add

```shell
$ git add a.html #a.html 파일만 추가
$ git add . #워킹 디렉토리 내 모든 파일을 추가
$ git add -i #명령 프롬프트에서 상호작용하며 추가(나갈 때 q 입력)
```

2. git commit

```shell
$ git commit -m "커밋 메세지" #간단한 커밋 메세지 입력 후, 커밋
```

3. git log

```shell
$ git log #커밋 이력 상세조회
$ git log --a.html #특정 파일의 변경 커밋 조회
```

4. git remote

```shell
$ git remote add origin <자신의 github원격저장소의 주소> #github 원격저장소와 연결/origin은 뒤에 쓴 github주소를 지칭하는 별칭(임의로 지정 가능)
$ git remote -v #연결된 원격저장소를 확인
```

5. git push

```shell
$ git push -u origin master #원격저장소에 저장/master는 branch의 이름이며, master는 remote repository를 생성하면 기본적으로 생성되는 브랜치. 브랜치는 독립적인 작업 공간을 의미. master가 아니라 다른 이름으로 하고 싶다면, 원하는 master자리에 (원하는 브런치명)을 넣으면 됨.
$ git push origin
```

