import time

# numpy
M = 1000000
t1 = time.time()
a1 = np.random.randint(1, 10, M)
a2 = np.random.randint(1, 10, M)
a3 = a1 + a2
t2 = time.time()
print(f'Numpy performance: {t2-t1}')
print(a3[:10])

# python
t1 = time.time()
a1 = [random.randint(1, 10) for _ in range(M)]
a2 = [random.randint(1, 10) for _ in range(M)]
a3 = [x1 + x2 for x1, x2 in zip(a1, a2)]
t2 = time.time()
