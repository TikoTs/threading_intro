import json
import threading
import time
import requests
import random

f = open('products.json', 'w')


lock = threading.Lock()
products = []
threads = []


def get_response(start_range, end_range):
    for i in range(start_range, end_range):
        url = "https://dummyjson.com/products/" + str(i)
        response = requests.get(url)
        r = response.json()
        with lock:
            products.append(r)



for i in range(0, 91, 10):
    t = threading.Thread(target=get_response, args=(i + 1, i + 11))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    time.sleep(random.randrange(0, 3))

json.dump(products, f, indent=4)

f.close()



