def solution(n):
	zeros = 0
	for i in n:
		if i == '0':
			zeros += 1
		else:
			break
	if zeros == len(n):
		return 1
	number = []
	for i in range(len(n)):
		number.append(int(n[i]))
	binary = []
	bits = 0
	while (zeros != len(number)):
		if number[len(number) - 1] % 2 != 0:
			binary.append(1)
		else:
			binary.append(0)
		bits += 1
		r = 0
		for i in range(zeros, len(number)):
			num = number[i]
			number[i] = num // 2 + r
			if i == zeros and number[i] == 0:
				zeros += 1
			r = 5 if num % 2 == 1 else 0
	cost = bits - 1
	for i in range(len(binary)):
		if binary[i] == 1:
			count = 1
			binary[i] = 0
			for j in range(i + 1, len(binary)):
				if binary[j] == 1:
					count += 1
					if j == len(binary) - 1:
						if count < 3:
							cost += 1
						else:
							cost += 2
						i = len(binary) - 1
					else:
						binary[j] = 0
				else:
					if count != 1:
						binary[j] = 1
					cost += 1
					i = j - 1
					break
	return cost

print(str(solution("15")))