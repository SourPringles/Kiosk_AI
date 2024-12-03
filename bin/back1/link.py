import mysql.connector

#MySQL 연결하기
def create_connection() :
    try :
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'rootpass',
            port = '3306',
            database = 'kiosk_',  # 본인의 DB 이름으로 수정
            auth_plugin='mysql_native_password'  # 인증 플러그인 명시
        )
        if conn.is_connected():  # 연결 성공 여부 확인
            print("MySQL 데이터베이스에 연결되었습니다.")
            print("MainPc")
            return conn
        
    except :
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'kiosk_proj',
            password = 'kiosk_pass',
            port = '3306',
            database = 'kiosk_',  # 본인의 DB 이름으로 수정
            auth_plugin='mysql_native_password'  # 인증 플러그인 명시
        )
        if conn.is_connected():  # 연결 성공 여부 확인
            print("MySQL 데이터베이스에 연결되었습니다.")
            print("SubPc")
            return conn

#커서 만들기
def cursor(conn):
    cursor = conn.cursor()
    return cursor

#MySQL 연결 끊기
def close_connection(conn):
    if conn.is_connected():
        conn.close()
        print("MySQL 데이터베이스와의 연결이 종료됨.")