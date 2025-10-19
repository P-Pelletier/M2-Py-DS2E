import time
from utils import f, iterable


if __name__ == "__main__":
    t = time.time()
    results = []
    for i in iterable:
        result = f(i)
        results.append(result)
    print('Took %.3f seconds' % (time.time() - t))