import time
from utils import f, n, workers
import ray

t = time.time()
ray.init(num_cpus = workers)
# @ray.remote
# def f(x):
#     time.sleep(1)
#     return x * x
f_remote = ray.remote(f)
futures = [f_remote.remote(i) for i in range(n)]
squares = ray.get(futures)
print('Took %.3f seconds' % (time.time() - t))