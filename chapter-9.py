def analyze_list(arr):
	counts = {}
	duplicates = set()
	
	for num in arr:
		if num in counts:
			counts[num] += 1
			duplicates.add(num)
		else:
			counts[num] = 1
	
	return duplicates, counts

# Example usage
input_list = [1, 2, 3, 2, 4, 5, 1]
duplicates, occurrences = analyze_list(input_list)

print(f"Duplicates are: {', '.join(map(str, duplicates))}")
for num, count in occurrences.items():
	print(f"{num}: {count} time{'s' if count > 1 else ''}")
