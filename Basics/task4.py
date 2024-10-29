from concurrent.futures import ThreadPoolExecutor

def task_1():
    print("Task 1 executed")

def task_2():
    print("Task 2 executed")


with ThreadPoolExecutor() as executor:
    future1 = executor.submit(task_1)
    future2 = executor.submit(task_2)