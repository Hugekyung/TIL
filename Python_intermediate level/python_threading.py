import threading

""" 간단한 스레드 사용 예시"""
def threading_sol():
    for i in range(1, 11):
        print(i)
    print("스레드 종료")

threading.Thread(target=threading_sol).start()
threading.Thread(target=threading_sol).start()