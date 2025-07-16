def reverse(num):
	reversed_num = 0
	while num > 0:
		digit = num % 10
		reversed_num = reversed_num * 10 + digit
		num = num // 10

	return reversed_num

num = int(input("Enter a number: "))
reversed_num = reverse(num)

if num == reversed_num:
	print(f"{num} is a palindrome.")
else:
	print(f"{num} is not a palindrome. Reversed number is {reversed_num}.")