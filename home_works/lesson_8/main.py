from home_works.lesson_8.server import *
from home_works.lesson_8.client import *
from threading import Thread


if __name__ == '__main__':
    print('Start total time!')
    start = time()
    server = Thread(target=server, args=())
    client = Thread(target=client, args=())
    server.start()
    client.start()
    server.join()
    client.join()
    print(f'Total time is: {time() - start}')
