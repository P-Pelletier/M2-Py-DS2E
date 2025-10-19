import time
from utils import f, workers, iterable
from joblib import Parallel, delayed


if __name__ == "__main__":
    t = time.time()
    results = Parallel(n_jobs=workers)(delayed(f)(i) for i in iterable)
    print('Took %.3f seconds' % (time.time() - t))
