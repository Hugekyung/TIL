# crontab
Crontab은 Cron + Table의 합성어인데 여기서 Cron은 유닉스 계열 컴퓨터 운영체제의 시간 기반 잡 스케줄러이다. 즉, Cron을 통해 소프트웨어 환경을 설정하고 관리할 목적으로 작업을 고정된 시간, 날짜, 간격에 주기적으로 스케줄링을 할 수 있게 한다.

Cron은 셸 명령어들이 주어진 일정에 주기적으로 실행하도록 규정해둔 Crontab 파일에 의해 구동된다. crontab 파일들은 잡 목록 및 cron 데몬에 대한 다른 명령들이 보관된 위치에 저장되어 있다. 사용자들은 자신들만의 개개의 crontab 파일들을 가질 수 있으며, 가끔은 /etc 또는 /etc의 하위 디렉터리에 시스템 관리자들만이 편집할 수 있는, 시스템 전반에 영향을 미치는 crontab 파일이 존재하는 경우도 있다.

# crontab 사용법
crontab 설정 편집
> crontab -e

crontab 파일 문법 체계
>┌───────────── min (0 - 59)  
>│ ┌────────────── hour (0 - 23)  
>│ │ ┌─────────────── day of month (1 - 31)  
>│ │ │ ┌──────────────── month (1 - 12)  
>│ │ │ │ ┌───────────────── day of week (0 - 6) (0 to 6 are     Sunday to Saturday, or use names; 7 is Sunday, the same as 0)  
>│ │ │ │ │  
>│ │ │ │ │  
>@ @ @ @ @  command to execute(@ == *)

# 사용예시
test.txt파일에 실행 권한 부여
>chmod +x test.txt

test.txt파일에 대해 group에 write 권한 부여
>chmod g+w test.txt

test.txt파일에 대해 others의 모든 권한 박탈
>chmod o-rwx test.txt