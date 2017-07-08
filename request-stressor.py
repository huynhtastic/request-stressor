"""
add async requesting
refactor to show time to request

"""
import requests
import threading
import timeit

def make_requests(i):
#    while True:
    start_time = timeit.default_timer()
    requests.get('http://www.projectonyx.io')
    exec_time = timeit.default_timer() - start_time
    print('Client {0:2} Response time: {1}'.format(i, exec_time))

def main():
    num_clients = 1000
    start_test = timeit.default_timer()
    for i in range(num_clients):
        t = threading.Thread(target=make_requests, args=(i,))
        t.start()
    exec_test = timeit.default_timer() - start_test
    print('{0} clients in {1} seconds'.format(num_clients, exec_test))

if __name__ == '__main__':
    main()
