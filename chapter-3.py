num = 12345

# Reverse the number
# reversed_num = int(str(num)[::-1])

reversed_num = 0
while num > 0:
	digit = num % 10  # Extract the last digit
	reversed_num = reversed_num * 10 + digit  # Append the digit to the reversed number
	num = num // 10  # Remove the last digit from the original number


print("Reversed number:", reversed_num)