from mergesort import mergesort
from generating import generate_dataset
import time


def test(start_size, max_size, start_range, stop_range):
    sizes = list()
    avg = list()
    size = start_size
    n=20
    while size < max_size:

        arr = generate_dataset(size, start_range, stop_range)
        total_time = 0

        for _ in range(n):
            arr_copy = arr.copy()
            start_time = time.time()
            mergesort(arr_copy)
            total_time += time.time() - start_time
        
        avg.append(total_time/n)
        sizes.append(size)
        print(f"T({size}) = {avg[-1]}")
        size*=2

    for i in range(len(avg)-1):
        print(f"T({sizes[i+1]})/T({ sizes[i] }) = {avg[i+1] / avg[i]}")

test(start_size=2**9, max_size=2**21, start_range=-100, stop_range=100)


