# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

nums1 = [0,1,2,3,4,5,6,7,8,9]

n=1
for i1 in nums1:
	nums2 = [x for x in nums1 if x != i1]
	for i2 in nums2:
		nums3 = [x for x in nums2 if x != i2]
		for i3 in nums3:
			nums4 = [x for x in nums3 if x != i3]
			for i4 in nums4:
				nums5 = [x for x in nums4 if x != i4]
				for i5 in nums5:
					nums6 = [x for x in nums5 if x != i5]
					for i6 in nums6:
						nums7 = [x for x in nums6 if x != i6]
						for i7 in nums7:
							nums8 = [x for x in nums7 if x != i7]
							for i8 in nums8:
								nums9 = [x for x in nums8 if x != i8]
								for i9 in nums9:
									nums10 = [x for x in nums9 if x != i9]
									if not n%1000000:
										print n
										print i1,i2,i3,i4,i5,i6,i7,i8,i9,nums10[0]
									n+=1
print n
