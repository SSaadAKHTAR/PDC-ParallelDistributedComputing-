import threading
import time

def calc_fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)


start_time = time.time()

threads = []
for i in range(3):  # 4 threads
    t = threading.Thread(target=calc_fibonacci, args=(30,))
    threads.append(t)

    print(f'Starting thread {i + 1}')
    t.start()

for t in threads:
    t.join()


end_time = time.time()

execution_time = end_time - start_time

print(f"Total execution time: {execution_time} seconds")
