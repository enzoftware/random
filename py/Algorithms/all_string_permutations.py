def all_string_permutations(s):
	res = []
	if len(s) == 1:
		res = [s]
	else:
		for i,c in enumerate(s):
			for perm in all_string_permutations(s[:i] + s[i+1: ]):
				res.append(s[i]+perm)

	return res

print(all_string_permutations('aaaaaaaaaaaaaaaaaaaaaaaaaaabc'))
	