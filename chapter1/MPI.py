from mpi4py import MPI 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size < 2:
    print("This program requires at least 2 processes!")
else:
    if rank == 0:
        data = {'key1': 'value1', 'key2': 'value2'}
        comm.send(data, dest=1)
        print("Sent data from process 0")
    elif rank == 1:
        data = comm.recv(source=0)
        print(f"Received data at process 1: {data}")
    else:
        print(f"Process {rank} is idle.")
