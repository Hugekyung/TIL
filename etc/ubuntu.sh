# 우분투 18.04 버전 루트계정 사용하기
"""우분투는 기본적으로 root 계정의 패스워드가 설정되어 있지 않습니다. 

우분투 설치시 관리자로 설정한 사용자로 `sudo` 명령어를 사용해서 root 권한을 사용하는 것이 바람직하지만,

여러가지 이유로 root 계정을 직접 사용하는 방법을 알아보겠습니다. 
"""

# 설정방법 : 우분투를 인스톨 하는 과정에서 추가한 계정을 이용하여 sudo 명령어로 root 권한을 얻을 수 있습니다. 
# 방법 1

ubuntu@localhost:~$ sudo -s
[sudo] password for ubuntu:  		# ubuntu 계정의 패스워드 입력
root@localhost:~#                   	# root계정으로 전환

# 방법 2

ubuntu@localhost:~$ sudo passwd root
[sudo] password for ubuntu:   		# ubuntu 계정 패스워드 입력
Enter new UNIX password:      		# root 계정 패스워드 설정
Retype new UNIX password:     		# 재입력
passwd: password updated successfully

ubuntu@localhost:~$ su -
Password:                     		# root 계정 패스워드 입력
root@localhost:~#             		# root 계정으로 전환

# su 명령어 실행 제한하기: root 계정은 모든 권한을 가진 전지전능한 계정이므로 절때 아무나 로그인할 수 있어서는 안됩니다. 
# 그래서 su 명령어를 특정 사용자나 그룹으로 제한하는 방법을 알아보겠습니다.

root@localhost:~# vi /etc/pam.d/su
# 아래 라인의 주석을 해제하고 su를 허가할 그룹을 기입합니다.
auth       required   pam_wheel.so  group=admingroup

root@localhost:~# usermod -G admingroup ubuntu