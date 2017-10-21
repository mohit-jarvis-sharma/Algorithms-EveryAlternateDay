#Dummy Set
my_set = [1,2,4,5,6,3]

# My Method: NoneType Errors :/
def gen_subsets2(some_set):
	my_subsets = []
	my_subsets.append([])
	for i in some_set:
		temp_set = []
		for j in my_subsets:
			temp_set.append(j.append(i))
		my_subsets.extend(temp_set)
		my_subsets.append([i])
	return my_subsets

# Bit Method
def gen_subsets(some_set):
	subset = []
	for i in range(2**len(some_set)):
		temp = str(bin(i))
		final_temp = temp[2:].zfill(len(some_set))
		temp_set = []
		for j,k in zip(final_temp,range(len(some_set))):
			tempJ = int(j)
			if tempJ:
				temp_set.append(some_set[k])
		subset.append(temp_set)
	return subset

print(gen_subsets(my_set))
# Complexity: O(n*2^n)