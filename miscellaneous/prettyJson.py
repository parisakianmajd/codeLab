#Pretty print a json object using proper indentation.

#Every inner brace should increase one indentation to the following lines.
#Every close brace should decrease one indentation to the same line and the following lines.
#The indents can be increased with an additional '\t'

def prettyJson(A):
    result = []
    if len(A) == 0:
        return result
    currentTab = 0
    i = 0
    if A[0] == '"':
        A = A[1:-1]
        
    while i < len(A):
        if A[i] in ["{", "["]:
            result.append(currentTab * '\t' + A[i])
            currentTab += 1
        elif A[i] in ["}", "]"]:
            currentTab -= 1
            if A[i + 1] == ",":
                result.append(currentTab * '\t' + A[i] + A[i+1])
                i += 1
            else:
                result.append(currentTab * '\t' + A[i])            
        else:
            word = ""
            while A[i] not in [",", "}", "]"]:
                word += A[i]
                i += 1
                if A[i] in ["{", "["]:
                    break
            if A[i] == ',':
                word += A[i]
            else:
                i -= 1
            result.append(currentTab * '\t' + word)
        i += 1
    return result



A1 = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
A2 = '["foo", {"bar":["baz",null,1.0,2]}]'
A = '"{"id":100,"firstName":"Jack","lastName":"Jones","age":12}"'
result = prettyJson(A)
for r in result:
    print r
