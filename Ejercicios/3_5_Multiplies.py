def sum_multipliers_3_5(n: int) -> int:
	return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])

print(sum_multipliers_3_5(1000))