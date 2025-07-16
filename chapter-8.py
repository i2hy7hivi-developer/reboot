def find_duplicates(arr):
	seen = set()
	duplicates = set()
	
	for num in arr:
		if num in seen:
			duplicates.add(num)
		else:
			seen.add(num)
	
	return duplicates

def count_occurrences(arr):
    counts = {}
    
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    return counts

# Example usage
input_list = [1, 2, 3, 2, 4, 5, 1]
duplicates = find_duplicates(input_list)
print(f"Duplicates are: {', '.join(map(str, duplicates))}")

input_list = [1, 2, 2, 3, 3, 3]
occurrences = count_occurrences(input_list)

for num, count in occurrences.items():
    print(f"{num}: {count} time{'s' if count > 1 else ''}")
