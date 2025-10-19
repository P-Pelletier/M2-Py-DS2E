import time
from utils import f, workers, iterable
from multiprocessing import Pool

if __name__ == "__main__":
    t = time.time()
    with Pool(workers) as p:
        results = p.map(f, iterable)
    print('Took %.3f seconds' % (time.time() - t))