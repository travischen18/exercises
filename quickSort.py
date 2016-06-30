def quickSort(list, begin, end):
	index = partition(list, begin, end)
	if begin < (index - 1):
		quickSort(list, begin, index - 1)
	if end > index:
		quickSort(list, index, end)

def partition(list, begin, end):
	pivot = list[(begin + end) / 2]

	while (begin <= end):
		while (list[begin] < pivot):
			begin = begin + 1

		while (list[end] > pivot):
			end = end - 1

		if begin <= end:
			swap(list, begin, end)
			begin = begin + 1
			end = end - 1

	return begin

def swap(list, first, second):
	temp = list[first]
	list[first] = list[second]
	list[second] = temp


list = [938, 5, 93, 40, 10, 108, 3, 9, 19, 22, 4]
quickSort(list, 0, len(list) - 1)
print list