"""
taken from engineering man's github
"""

from multiprocessing import Process
import os
import math

def calc():
    for i in range(0, 8800000):
        math.sqrt(i)

processes = []

for i in range(os.cpu_count()):
    print('registering process %d' % i)
    processes.append(Process(target=calc))

for process in processes:
    process.start()

for process in processes:
    process.join()
