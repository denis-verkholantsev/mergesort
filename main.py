from mergesort import mergesort
from generating import generate_dataset
import time
import matplotlib.pyplot as plt
from math import log2


def func1(n):
    return 2*n * log2(2*n) / (n * log2(n))


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
    
    return sizes, avg



n_vals, time_vals = test(start_size=2**9, max_size=2**21, start_range=-100, stop_range=100)

actual_values = [time_vals[i+1] / time_vals[i] for i in range(len(time_vals)-1)]
priori_values = [func1(el) for el in n_vals[:-1]]


plt.figure(figsize=(10, 6))
plt.plot(n_vals[:-1], priori_values, color="red", label='2n*log2(2n)/(n*log2(n))')
plt.plot(n_vals[:-1], actual_values, color="blue", label='actual')
plt.ylim(0, 3)
plt.xlabel('log(n)')
plt.xscale('log') 
plt.ylabel('func(n)')
plt.legend()
plt.grid(True)
plt.savefig('plot1.png')