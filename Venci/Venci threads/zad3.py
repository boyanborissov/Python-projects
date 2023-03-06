#Пример 3: Масив (списък) от нишки:
import threading
import time

def printMsg(n):
    time.sleep(0.5)
    print(f'[{n}] Hello')

def main():
    count = 5
    threads = []
    for i in range(5):
        t = threading.Thread(target=printMsg(i,))
        threads.append(t)
        t.start()

        for t in threads:
            t.join()

        print('Main complete!')

if __name__ == '__main__':
    main()