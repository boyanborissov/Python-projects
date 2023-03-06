#Пример 2: Нишки - подаване на аргументи:
import threading
import time

def printMsg(text, count, delay):
    #print(f'Start thread{threading.get_ident()}:')
    for i in range(count):
        print(text)
        time.sleep(delay)
    # print(f'Thread{threading.get_ident()} complete!')

def main():
    #t1 = threading.Thread(target=printMsg, args=("UKTC", 10, 0.1))
    t1 = threading.Thread(target=printMsg('UKTC',10,0.1))
    t2 = threading.Thread(target=printMsg('Pravets',10,0.5))
    t3 = threading.Thread(target=printMsg('Sofia',10,0.7))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('Main complete!')

if __name__ == '__main__':
    main()