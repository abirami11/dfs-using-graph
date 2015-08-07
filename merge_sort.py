def merge_sort(alist):
	if len(alist) < 2 :
		 return list(alist)
	middle = len(alist)//2
	lefthalf = alist[:middle]
	righthalf = alist[middle:]

	return merge(merge_sort(lefthalf),merge_sort(righthalf))
	 

def merge(left,right):
	list1 = []
	i = 0
	j = 0
	while i < len(left) and j < len(right):
			if left[i] < right[j] :
				list1.append(left[i])
				i=i+1
			else:
				list1.append(right[j])
				j=j+1
	while j < len(right) :
		list1.append(right[j])
		j=j+1
	while i < len(left):
		list1.append(left[i])
		i=i+1
	#print list1
	return list1

alist = [5,4,3,2,1,6]
print merge_sort(alist)
#merge_sort(alist)
#merge([5,3],[4])