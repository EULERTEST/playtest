import p2


# test illegal input
def test_neg():
	Range = -1
	assert p2.sumFibs(Range) == 0

# test input 1, return 0, bcs 1 is not even.
def test_1():
	Range = 1
	assert p2.sumFibs(Range) == 0

# test input 2, return 0, bcs 2 is not included for the input range.
def test_2():
	Range = 2
	assert p2.sumFibs(Range) == 0

# test input 10, return 10, bcs [2,8] are even.
def test_10():
	Range = 10
	assert p2.sumFibs(Range) == 10

# test input 100, return 44, bcs [2,8,34] are even from the question.
def test_100():
	Range = 100
	assert p2.sumFibs(Range) == 44
