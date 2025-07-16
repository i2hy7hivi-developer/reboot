def find_missing_number(arr):
	# Calculate the expected sum of numbers from 1 to n
	n = len(arr) + 1
	expected_sum = n * (n + 1) // 2
	
	# Calculate the actual sum of the array
	actual_sum = sum(arr)
	
	# The missing number is the difference
	return expected_sum - actual_sum

# Example usage
input_list = [1, 3, 4, 5]
missing_number = find_missing_number(input_list)
print(f"{missing_number} is missing")