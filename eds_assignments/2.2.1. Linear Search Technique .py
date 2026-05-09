def linear_search(arr , search):
	for i in range(len(arr)):
		if arr[i]== search:
			return i
	return -1
arr = list(map(int, input().split()))
search = int(input())
result = linear_search(arr , search)
if result == -1:
	print("Not found")
else:
	print(result)