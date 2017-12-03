from itertools import combinations, permutations

def combine(arr,n):
    if not n:
        return [[]]
    if not arr:
        return []

    head = [arr[0]]
    tail = arr[1:]
    new_comb = [head + lst for lst in combine(tail, n - 1)]

    return new_comb + combine(tail,n)

def permute(s):
   if len(s) == 1:
     return [s]

   perm_list = [] 
   for a in s:
     remaining_elements = [x for x in s if x != a]
     other_permutes = permute(remaining_elements) 

     for p in other_permutes:
       perm_list.append([a] + p)

   return perm_list


print combine(range(1,5),2)
print list(combinations(range(1,5),2))
print permute([1,2,3])
print list(permutations([1,2,3]))
