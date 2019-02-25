import math
import random
import sys

def generate_pi(iterations=100000):
	count_coprime = 0
	for _ in range(iterations):
		rand_1 = random.randint(1, sys.maxsize)
		rand_2 = random.randint(1, sys.maxsize)
		if math.gcd(rand_1, rand_2) == 1:
			count_coprime += 1
	return math.sqrt(6 / (count_coprime / iterations))

pi = generate_pi()
print(pi)
