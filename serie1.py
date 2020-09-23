n = int(input("Enter value for n : ")) # List size
i = 0 # Counter representing the current position in the subsequence (the decimal representation of the binary number we will write)
l = 1 # Counter representing the current length of the word we are writing (the length of each element in the subsequence)

A = []; # Empty list

while(len(A) < n): # The list is bounded by n, we will not keep computing the list any further
	for i in range(0, pow(2,l)): # Each subsequence has a length of 2^l - 1, so we loop through it from 0 to 2^l
		A.append(format(i, '0' + str(l) + 'b')) # Adding the number to the list, after having converted into binary format ; the format() function is useful to add the exact number of leading zeros and does the binary conversion itself
	l += 1

print("The nth element of A* is '" + A[-1] + "'")