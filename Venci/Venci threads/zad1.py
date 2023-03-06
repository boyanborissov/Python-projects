#Пример 1: Две нишки
import threading
import time

def printHello():
    print('Start thread 1:')
    for i in range(10):
        print('Hello')
        time.sleep(0.1)
    print('Thread 1 complete!')

def printUKTC():
    print('Start thread 2:')
    for i in range(10):
        print('UKTC')
        time.sleep(0.5)
    print('Thread 2 complete!')

def main():
    t1 = threading.Thread(target=printHello)
    t2 = threading.Thread(target=printUKTC)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Main complete!')

if __name__ == '__main__':
    main()


