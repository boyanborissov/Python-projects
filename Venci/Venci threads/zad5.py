#Пример 5: Семафори:
import threading
import time
import random

sem = threading.Semaphore(2)

def parking(n):
    print(f'[{n}] Waiting for parking...')
    sem.acquire()
    print(f'[{n}] In parking!')
    time.sleep(random.randint(1,5))
    print(f'[{n}] Out of parking!')
    sem.release()

def main():
    n = 10
    cars = []
    for i in range(n):
        t = threading.Thread(target=parking(i,))
        t.start()
        cars.append(t)

    for car in cars:
        car.join()

    print('Main complete!')

if __name__ == '__main__':
    main()