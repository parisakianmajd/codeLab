#Pretty print a json object using proper indentation.

#Every inner brace should increase one indentation to the following lines.
#Every close brace should decrease one indentation to the same line and the following lines.
#The indents can be increased with an additional '\t'

def prettyJson(A):
    ret = []
    n = len(A)
    if n == 0:
        return ret
    noOfIndents = 0
    temp = ""    
    for i in range(n):
        if A[i] != ' ':
            temp += A[i]
        if A[i] in ['{', '[']:
            if len(temp) > 2 and temp[-2] != '\t':
                ret.append(temp[:-1])
            temp = "\t" * noOfIndents + temp[-1]
            ret.append(temp)
            noOfIndents += 1
            temp = "\t" * noOfIndents
        elif A[i] in ['}', ']']:
            noOfIndents -= 1
            if len(temp) > 2 and temp[-2] != '\t':
                ret.append(temp[:-1])
            temp = "\t" * noOfIndents + temp[-1]
        elif A[i] == ',':
            ret.append(temp)
            temp = "\t" * noOfIndents
    if len(temp) > 0 and temp[-1] != '\t':
        ret.append(temp)
    return ret



A1 = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
A2 = '["foo", {"bar":["baz",null,1.0,2]}]'
A3 = '"{"id":100,"firstName":"Jack","lastName":"Jones","age":12}"'

A = '{"id":100, "firstName":"Jack", "lastName":"Jones", "age":12}'
result = prettyJson(A3)
for r in result:
    print r
