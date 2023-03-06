#Пример 4: Race condition:
import threading
import time

value = 0;
lock = threading.Lock()

def add_value(amount, repeat):
    global value
    for i in range(repeat):
        lock.acquire()
        value += amount
        lock.release()

def sub_value(amount, repeat):
    global value
    for i in range(repeat):
        lock.acquire()
        value -= amount
        lock.release()

def main():
    adders = threading.Thread(target=add_value(100,10))
    subers = threading.Thread(target=sub_value(10,10 ))
    adders.start()
    subers.start()
    adders.join()
    subers.join()
    print(f'Value = {value}')

if __name__ == '__main__':
    main()
