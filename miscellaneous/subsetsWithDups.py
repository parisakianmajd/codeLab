#Given a collection of integers that might contain duplicates, S, return all possible subsets.



def helper(nums):
        if not nums:
            return [[]]
        else:
            first = nums[0]
            subs = helper(nums[1:])
            newl = []
            for i in subs:
                if i not in newl:
                    newl.append(i)
                l = [first]+i
                if l not in newl:
                    newl.append(l)
            return newl

def subsetsWithDup(A):
    A.sort()
    return sorted(helper(A))


def subsetsWithDup2(A):
    result = []
    subsetsWithDupRecu(result, [], sorted(A))
    return sorted(result)

def subsetsWithDupRecu(result, cur, nums):
    if not nums:
        if cur not in result:
            result.append(cur)
    else:
        subsetsWithDupRecu(result, cur, nums[1:])
        subsetsWithDupRecu(result, cur + [nums[0]], nums[1:])
