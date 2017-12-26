#Given a digit string, return all possible letter combinations that the number could represent.

#Use a mapping of digit to letters just like on the telephone buttons 

def letterCombinations(A):
    letters = {0: ["0"], 1:["1"], 2:["a", "b", "c"], 3:["d", "e", "f"],\
    4: ["g", "h", "i"], 5:["j", "k", "l"], 6: ["m", "n", "o"],\
    7: ["p", "q", "r", "s"], 8:["t", "u", "v"], 9:["w", "x", "y", "z"]}
    stack = [""]
    if len(A) == 0:
        return letters[0]
    if len(A) == 1:
        return letters[int(A)]
    for a in A:
        current = []
        while stack:
            current.append(stack.pop())
        for l in letters[int(a)]:
            for c in current:
                stack.append(c + l)
    out = []
    while stack:
        out.append(stack.pop())
    return sorted(out)


def letterCombinations2(A):
    table = {0: ["0"], 1:["1"], 2:["a", "b", "c"], 3:["d", "e", "f"],\
    4: ["g", "h", "i"], 5:["j", "k", "l"], 6: ["m", "n", "o"],\
    7: ["p", "q", "r", "s"], 8:["t", "u", "v"], 9:["w", "x", "y", "z"]}
    ans=[]
    if len(A)==1:
        return table[int(A[0])]
    for j in table[int(A[0])]:
        temp=letterCombinations(A[1:])
        for i in temp:
            ans.append(j+i)
    return ans

print letterCombinations("23")
print letterCombinations2("23")

