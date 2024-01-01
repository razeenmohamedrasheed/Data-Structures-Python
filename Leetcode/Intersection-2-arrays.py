nums1 = [1,2,2,1]
nums2 = [2,2]

result = [value for value in nums1 if value in nums2]
result = list(set(result))
print(result)