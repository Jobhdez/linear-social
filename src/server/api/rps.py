from src.python_client.client import compute
import timeit

def compute_lalg():
    compute('[[1 2 3] [4 5 6]] * [[7 8] [9 10] [11 12]]',
            'jobpink',
            'hello123')
    
def measure_rps(num_requests, fn):
    total_time = timeit.timeit(fn, number=num_requests)
    rps = num_requests / total_time
    return rps

num_requests = 100

rps = measure_rps(num_requests, compute_lalg)
print(f'requests per second: {rps}')
