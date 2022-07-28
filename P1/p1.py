# Q: Find the sum of all the multiples of 3 or 5 below natural number 1000 (https://projecteuler.net/problem=1)
# python version: python3


# TESTNUM: any natural number, range number is not included.
TESTNUM = 1000


def sumNNs(RANGE):
	workset = set()
	if(RANGE < 1):
		print("Illegal input, only natural number allowed!")
		return 0;
	else:
		for x in range(1, RANGE):
			if (x % 3 == 0 or x % 5 == 0):
				workset.add(x)

		total = sum(workset)
		return total

print(sumNNs(TESTNUM))