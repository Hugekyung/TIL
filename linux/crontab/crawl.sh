#!/bin/sh
PATH=$PATH:/home/ubuntu/workspace/env/bin # 스크래피를 실행하기 위한 가상환경 접속
export PATH
cd /home/ubuntu/workspace/sooing/sooing/spiders # 스크래피 실행 파일이 있는 디렉토리 이동
scrapy crawl crontabtest # 스크래피 실행