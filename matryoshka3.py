def find_consecutive_runs(l):
	if not isinstance(l, list):
		return None
	results = [ind for ind, x in enumerate(l) if ind < len(l) - 2 and abs(l[ind] - l[ind + 1]) == 1 and abs(l[ind+1] - l[ind+2]) == 1 and l[ind] != l[ind+2]]
	if len(results):
		return results
	return None
