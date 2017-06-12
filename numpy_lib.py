# -*- coding=utf-8 -*-
from __future__ import print_function
import numpy as np
import numpy.random as random

# a = [1, 2, 3, 4]
# b = np.array(a)
# print(type(b))

# print(b.shape)
# print(b.argmax())
# print(b.max())
# print(b.mean())

# c = [[1, 2], [3, 4]]
# d = np.array(c)
# print(d.shape)
# print(d.size)
# print(d.max(axis = 0))
# print(d.max(axis = 1))
# print(d.mean(axis = 1))
# print(d.flatten())
# print(np.ravel(c))

# e = np.ones((3, 3), dtype = np.float)

# f = np.repeat(3, 4)

# g = np.zeros((2, 2, 3), dtype = np.uint8)
# g.shape
# h = g.astype(np.float)

# l = np.arange(10)
# m = np.linspace(0, 6, 5)

# p = np.array(
# 	[[1, 2, 3, 4],
# 	 [5, 6, 7, 8]]
# )

# print(p.shape)
# np.save('output/p.npy', p)
# q = np.load('output/p.npy')

random.seed(234)

random.rand(1, 3)

random.random()

normal = random.normal(size=(5, 2))
print(normal)

a = np.arange(10)

print(a)
random.shuffle(a)
print(a)

print(random.choice(a, 7))

print(random.choice(a, 7, replace=False))

b = random.permutation(a)

print(b)

print(random.bytes(16))