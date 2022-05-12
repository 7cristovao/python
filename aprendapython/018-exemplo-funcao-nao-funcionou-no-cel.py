import math

def is_prime(num):
	if num % 2 == 0 and num > 2:
		return False
	for i in range(3, int(math.sqrt(num)) + 1, 2):
		if num % i == 0:
			return False
	return True

is_prime(11)