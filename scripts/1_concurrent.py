import time
from utils import f, workers, iterable
import concurrent.futures

def main(n):
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(f, iterable))
    return results

if __name__ == '__main__':
    t = time.time()
    results = main(n)
    print('Took %.3f seconds' % (time.time() - t))
