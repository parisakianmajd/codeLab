#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

#e.g. n = 3:

#"((()))", "(()())", "(())()", "()(())", "()()()"
def helper(n):
    if n in helper.sequences:
        return helper.sequences[n]
    if n == 0:
        helper.sequences[0] = ['']
        return ['']

    seq = []
    for i in range(n):
        in_seq = helper(i)
        out_seq = helper(n-i-1)
        seq.extend(['(' + in_s + ')' + out_s for in_s in in_seq for out_s in out_seq])
    helper.sequences[n] = seq
    return seq

def generateParenthesis(n):
    helper.sequences = {}
    seq = helper(n)
    return sorted(seq)
    

def generateParenthesis2(n):
    stack = []
    stack.append( ('',0,0) )
    ans = []
    while( len(stack)!= 0):
        # pop from stack, make children, push into stack.
        s,o,c = stack.pop()
        if o==n and c==n:
            ans.append(s)
            continue
        if o<n:
            stack.append( (s+'(', o+1, c) )
        if c<o and c<n:
            stack.append( (s+')', o, c+1) )
    ans.reverse()
    return ans

print (generateParenthesis(4))
print (generateParenthesis2(4))

