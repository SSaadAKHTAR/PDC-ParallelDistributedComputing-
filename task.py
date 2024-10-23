from do_something import *  # Assuming you have a function do_something
import time
import multiprocessing
import threading

if __name__ == "__main__":
    size = 100000
    procs = 10
    jobs = []

    # Multiprocessing
    start_time = time.time()
    out_list = [[] for i in range(procs)]
    
    for i in range(procs):
        process = multiprocessing.Process(target=do_something, args=(size, out_list[i]))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.time()
    print("Multiprocessing time =", end_time - start_time)

    # Reset jobs list for threading
    jobs = []
    threads = 10
    start_time = time.time()
    out_list = [[] for i in range(threads)]

    for i in range(threads):
        thread = threading.Thread(target=do_something, args=(size, out_list[i]))  # Corrected to pass the function reference
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete.")
    end_time = time.time()
    print("Multithreading time =", end_time - start_time)
