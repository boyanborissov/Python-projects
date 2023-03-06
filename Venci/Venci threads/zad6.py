#Пример 6: Синхронизация на нишки:
import threading
import time
import random

sem = threading.Semaphore(0)

def startMachine():
    time.sleep(4)
    print('Machine start...')
    sem.release()
    time.sleep(1)
    print('Start procedure finished')

def workMachine():
    print('Ready to start working...')
    sem.acquire()
    print('Working...')

def main():
    t1 = threading.Thread(target=startMachine)
    t2 = threading.Thread(target=workMachine)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()