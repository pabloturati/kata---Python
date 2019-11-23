
def count_occurance(e, arr):
  count = 0
  for index, value in enumerate(arr):
    if value == e: count+=1
  return count


def find_it(A):
  uniqueArr = set(A)
  for val in uniqueArr:
    if count_occurance(val, A) % 2 > 0:
      return val



A = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

test = find_it(A)
print(test)