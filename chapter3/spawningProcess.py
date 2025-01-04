import multiprocessing

def myFunc(i):
    print('Calling myFunc from process n°: %s' % i)
    for j in range(i):
        print('Output from myFunc is: %s' % j)

if __name__ == '__main__':
    processes = []  # List to keep track of processes
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        processes.append(process)  # Add the process to the list

    # Start and join each process
    for process in processes:
        process.start()

    for process in processes:
        process.join()
