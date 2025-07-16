def find_duplicates(arr):
	seen = set()
	duplicates = set()
	
	for num in arr:
		if num in seen:
			duplicates.add(num)
		else:
			seen.add(num)
	
	return duplicates

# Example usage
input_list = [1, 2, 3, 2, 4, 5, 1]
duplicates = find_duplicates(input_list)
print(f"Duplicates are: {', '.join(map(str, duplicates))}")

# ✔️ Time Complexity: O(n)
# ✔️ Space Complexity: O(n) (for set)
# ✔️ No nested loops — efficient!