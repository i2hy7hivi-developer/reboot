num = 19

if num == 0 or num == 1:
	print("{} is neither prime nor composite".format(num))
elif num > 1:
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			print("{} is not a prime number".format(num))
			break
	else:
		print("{} is a prime number".format(num))
else:
	print("{} is not a prime number".format(num))