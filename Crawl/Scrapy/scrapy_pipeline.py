"""database에 연결하고 크롤링한 데이터들을 db에 insert하기 위한 Pipeline.py 파일."""
"""settings.py에 ITEM_PIPELINES도 활성화해야 한다."""
from itemadapter import ItemAdapter
import MySQLdb # 해당 모듈을 설치해야 한다.


class Pipeline(object):
    host = host
    user = username
    password = password
    db_name = db_name

    def __init__(self):
        self.connection = MySQLdb.connect(self.host,
                                        self.user,
                                        self.password,
                                        self.db_name,
                                        charset="utf8mb4", # 생성한 db의 캐릭터셋
                                        use_unicode=True)
        self.cursor = self.connection.cursor()
        print("DB 정상 접속.")

    def process_item(self, item, spider):
        try:
            query = """INSERT INTO influencer(insta_id, username, follower, post_id, comments_count, likes_count, post_date) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")""".format(
                item['insta_id'], item['username'], item['follower'], item['post_id'], item['comments_count'], item['likes_count'], item['post_date']
                )

            # 해당 데이터가 db안에 없으면 insert하고, 있으면 새로운 데이터로 update를 하는 구문.
            # INSERT INTO 테이블 (컬럼1, 컬럼2, 컬럼3, ...) 
            # VALUES (컬럼1 데이터, 컬럼2 데이터, 컬럼3 데이터, ...) 
            # ON DUPLICATE KEY UPDATE 컬럼1={컬럼1 데이터}, 컬럼2={컬럼2 데이터}, 컬럼3={컬럼3 데이터}
            query_post = """INSERT INTO post (unique_id, post_id, comments_count, likes_count, post_date) VALUES ("{}", "{}", "{}", "{}", "{}") ON DUPLICATE KEY UPDATE
                                    comments_count="{}", likes_count="{}"
                                """.format(
                item['unique_id'], item['post_id'], item['comments_count'], item['likes_count'], item['post_date'], 
                item['comments_count'], item['likes_count']
                )

            self.cursor.execute(query) # 쿼리 실행
            self.connection.commit() # db 커밋
            print(f"{item['insta_id']}의 데이터가 정상적으로 INSERT 되었습니다.")
        except MySQLdb.Error as e:
            print("Error {}: {}".format(e.args[0], e.args[1]))
            return item