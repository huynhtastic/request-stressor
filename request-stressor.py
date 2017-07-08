import requests
import threading

def make_requests(i):
    while True:
        print(i, requests.get('http://www.projectonyx.io'))

def main():
    for i in range(40):
        t = threading.Thread(target=make_requests, args=(i,))
        t.start()

print(__name__)        
        
if __name__ == '__main__':
    main()
