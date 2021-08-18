# linux 기초 문법

linux에서 사용 가능한 기초 문법 정리.



## 현재 폴더 위치

- pwd(print working directory)

```shell
$ pwd

$ pwd . # 현재 디렉토리 파일탐색기 열기
```
  


## 폴더 변경

- cd(change directory)

```shell
$ cd <이동하고 싶은 폴더이름>

$ cd .. # 상위 디렉토리 이동

$ cd - # 이전 디렉토리 이동

$ cd ~ # 현재 경로의 최상위 디렉토리 이동
```



## 폴더, 파일 리스트 출력

- ls(list)

```shell
$ ls -a # 숨김파일까지 출력

$ ls -l # 파일의 자세한 정보 출력

$ ls -al # 숨김파일을 포함한 모든 파일의 자세한 정보 출력
```



## 파일&디렉토리 생성

- touch
- mkdir
- echo(문자 출력용 커맨드이지만 옵션과 사용하면 파일 생성도 가능)

```shell
$ touch <생성할 파일이름>

$ mkdir <생성할 디렉토리 이름>

$ echo "hello" > hello.txt # hello.txt 파일이 없으면 새로 만들고 "hello"라는 내용을 추가하고, 파일이 존재하면 "hello"를 덮어씌움

$ echo "hello" >> hello.txt # hello.txt의 기존 내용에 "hello"라는 새로운 내용을 추가(append)
```



## 파일 내용 확인

- cat

```shell
$ cat hello.txt # hello.txt의 내용 확인(출력)
```



## 파일 복사, 이동, 삭제

- cp
- mv
- rm
  - 만약 폴더를 삭제하고 싶다면 -r 옵션을 추가해서 삭제 가능.

```shell
$ cp <파일이름> <복사하고자 하는 경로>

$ mv <파일이름> <이동하고자 하는 경로>

$ rm <삭제하고 싶은 파일이름>

$ rm -r <삭제하고 싶은 디렉토리 이름>
```



## 특정 문자가 포함된 파일 찾기

- grep

```shell
$ grep "world" *.txt # "world"라는 단어가 들어 있는 txt파일 출력

$ grep -n "world" *.txt # 몇 번째 줄에 있는지 함께 출력

$ grep -ni "world" *.txt # 대소문자 관계없이 모두, 몇 번째 줄에 등장하는지 출력
```



## 특정 포맷의 파일 찾기

- find

```shell
$ find . -type file -name "*.txt" # 현재 디렉토리부터 하위 디렉토리까지 txt형식의 파일을 모두 찾아 출력

$ find . -type directory -name "*2" # 현재 디렉토리부터 하위 디렉토리까지 이름이 2로 끝나는 디렉토리를 찾아 출력
```