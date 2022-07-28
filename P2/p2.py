# Q: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. (https://projecteuler.net/problem=2)
# python version: python3

# TESTNUM: start from 3, range number is not included.
TESTNUM = 4*(10**6)


def sumFibs(RANGE):
	# return 0 for numbers smaller than 3. They are either illegal input, or not included in the sum of even.
	if(RANGE <= 0):
		print("Illegal input, only natural number allowed!")
		return 0
	elif(RANGE < 3):
		return 0
	else:
		a = 1
		b = 2
		total = 2

		# initially plan fib[1] + fib[2] directly, however, too many numbers in the list if so.
		for x in range(3, RANGE):
			c = a + b
			a = b
			b = c

			if(c >= RANGE):
				break

			# print(c)
			# the RANGE is not included, thus, sum c only after ensure it is in the RANGE.
			if(c % 2 == 0):
				print(c)
				total = total + c

		return total

print(sumFibs(TESTNUM))