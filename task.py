import threading
import time
import requests

start = time.time()


class UrlThread(threading.Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        requests.get(self.url)


th1 = UrlThread('https://google.com/')
th2 = UrlThread('https://google.com/')
th3 = UrlThread('https://google.com/')

th1.start()
th2.start()
th3.start()

url = time.time()-start
print(f'Время выполнения программы (запрос GET, на потоках) {url}')

start = time.time()


def without_threads():
    requests.get('https://google.com/')
    requests.get('https://google.com/')
    requests.get('https://google.com/')


w_url = time.time()-start
print(f'Время выполнения программы (запрос GET) {w_url}')
