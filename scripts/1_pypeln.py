import time
from utils import f, workers, iterable
import pypeln as pl


if __name__ == "__main__":
    t = time.time()
    stage = pl.process.map(f, iterable, workers=workers, maxsize=workers+1)
    results = list(stage) 
    print('Took %.3f seconds' % (time.time() - t))
# In pypeln, maxsize controls the size of the internal input buffer for a stage. It limits how many data items can be "waiting in line" to be processed by the workers.

# This is a mechanism for applying backpressure, which prevents a fast-producing stage from overwhelming a slow-consuming stage with too much data, which could exhaust your computer's memory.

# ☕ The Coffee Shop Analogy

# Think of a pypeln stage as a small coffee shop to help understand the parameters:

#     data = range(10): These are the 10 customers arriving at your shop.

#     workers=3: You have 3 baristas working.

#     slow_add1: This is the slow process of making a coffee drink.

#     maxsize=4: This is the crucial part. It's the maximum number of people allowed inside the shop's waiting area at one time.

# Here's how it plays out with maxsize=4:

#     The first 3 customers from data (0, 1, 2) come in and are immediately served by the 3 available baristas.

#     The 4th customer (3) comes in and stands in the one available spot in the waiting area (the input queue). The shop is now at its maximum capacity of 4 (3 being served + 1 waiting).

#     The 5th customer (4) arrives but must wait outside. The range iterable is blocked. It cannot push more customers into the shop because the waiting area is full.

#     One of the baristas finishes making a coffee (slow_add1 returns a value). This frees up a spot.

#     The 5th customer (4) can now enter the shop and wait for the newly freed barista.

#     This process continues. A new customer is only allowed to enter the shop when another customer's order is complete, ensuring the waiting area never exceeds its maxsize.

# ## Why Use maxsize?

# The primary reason to use maxsize is memory management. 🧠

# Imagine if data was a generator yielding millions of large objects (like high-resolution images) and the slow_add1 function was very slow (e.g., complex image processing).

#     Without maxsize (or maxsize=0): The generator would run very fast, pushing millions of images into the stage's internal queue. The slow workers wouldn't be able to keep up. This queue would grow enormous, potentially consuming all of your system's RAM and crashing the program.

#     With maxsize: By setting maxsize=100, for example, you guarantee that no more than 100 images will ever be loaded into memory waiting for the workers. The fast generator is forced to pause (backpressure) until the slow workers catch up, creating a stable, memory-efficient pipeline.