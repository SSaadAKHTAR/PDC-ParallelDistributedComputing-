import multiprocessing

def create_items(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        output_pipe.send(item)  # Send items through the pipe
    output_pipe.close()  # Close the output pipe after sending all items

def multiply_items(pipe_1, pipe_2):
    _, input_pipe = pipe_1
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()  # Receive item from the input pipe
            output_pipe.send(item * item)  # Send squared item through the output pipe
    except EOFError:
        output_pipe.close()  # Close the output pipe when input is exhausted

if __name__ == '__main__':
    # Create the first pipe
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(
        target=create_items, args=(pipe_1,))
    process_pipe_1.start()

    # Create the second pipe
    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(
        target=multiply_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()

    # Close the unused ends of the pipes in the main process
    pipe_1[0].close()
    pipe_2[0].close()

    # Receive and print the processed items
    try:
        while True:
            print(pipe_2[1].recv())  # Read from the second pipe
    except EOFError:
        print("End of processing")
    
    # Ensure child processes complete
    process_pipe_1.join()
    process_pipe_2.join()
