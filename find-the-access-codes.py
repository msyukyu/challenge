def solution(l):
	dic = {}
	for i in range(len(l) - 1, -1, -1):
		dic[i] = []
		for j in range(i - 1, -1, -1):
			if l[i] % l[j] == 0:
				dic[i].append(j)
	count = 0
	for i in dic:
		for j in dic[i]:
			count += len(dic[j])
	return count

print(str(solution([1, 2, 3, 4, 5, 6])))