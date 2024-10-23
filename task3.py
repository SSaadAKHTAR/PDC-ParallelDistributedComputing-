import numpy as np
import time

# Define the size of the vectors
N = 1000000

# Initialize random vectors a and b
a = np.random.random(N).astype(np.float32)
b = np.random.random(N).astype(np.float32)

# Start timing
start_time = time.time()

# Vector addition using data parallelism (NumPy)
c = a + b  # NumPy takes care of parallelism internally

# End timing
end_time = time.time()

# Print time taken and the first 10 elements of the result
print(f"Time taken for data parallel computation (NumPy): {end_time - start_time:.5f} seconds")
print(f"First 10 elements of result: {c[:10]}")
