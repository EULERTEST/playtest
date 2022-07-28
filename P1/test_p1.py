import p1

# test illegal input
def test_neg():
	Range = -1
	assert p1.sumNNs(Range) == 0

def test_1():
	Range = 1
	assert p1.sumNNs(Range) == 0

# sum of [3,5,6,9]
def test_10():
	Range = 10
	assert p1.sumNNs(Range) == 23

# sum of [3,5,6,9,10,12]
def test_15():
	Range = 15
	assert p1.sumNNs(Range) == 45

# sum of [3,5,6,9,10,15]
def test_16():
	Range = 16
	assert p1.sumNNs(Range) == 60