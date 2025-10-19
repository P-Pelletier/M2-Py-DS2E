import time
from utils import f, workers, iterable
from mpire import WorkerPool



if __name__ == "__main__":
    t = time.time()
    with WorkerPool(n_jobs=workers) as pool:
        results = pool.map(f, iterable)
    print('Took %.3f seconds' % (time.time() - t))
