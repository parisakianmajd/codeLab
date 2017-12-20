#Given an array of real numbers greater than zero in form of strings.
#Find if there exists a triplet (a,b,c) such that 1 < a+b+c < 2 . 
#Return 1 for true or 0 for false

def tripleSum(A):
        res = [float(A[0]), float(A[1])]
        for i in range(2, len(A)):
                res.append(float(A[i]))
                if sum(res) < 1:
                        res.remove(min(res))
                        continue
                if sum(res) > 2:
                        res.remove(max(res))
                        continue
                if sum(res) >1 and sum(res) < 2:
                        return 1 
        return 0

#https://www.quora.com/Given-n-positive-real-numbers-find-whether-there-exists-a-triplet-among-this-set-such-that-the-sum-of-the-triplet-is-in-the-range-1-2-Do-it-in-linear-time-and-constant-space

def tripleSum2(self, A):
        n = len(A)
        A = map(float, A)
        buckets = [[], [], []]
        for a in A:
            if i < 2.0/3:
                buckets[0].append(a)
            elif i < 1:
                buckets[1].append(a)
            else:
                buckets[2].append(a)

        def get(index):
            max1, max2, max3 = 0, 0, 0
            min1, min2, min3 = 2, 2, 2
            for i in buckets[index]:
                if i > max1:
                    max1, max2, max3 = i, max1, max2
                elif i > max2:
                    max2, max3 = i, max2
                elif i > max3:
                    max3 = i
                if i < min1:
                    min1, min2, min3 = i, min1, min2
                elif i < min2:
                    min2, min3 = i, min2
                elif i < min3:
                    min3 = i
            return [max1, max2, max3, min1, min2, min3]
        # A = (0, 2/3]
        # B = [2/3, 1)
        # C = [1, 2)

        # Possible Cases
        #AAA AAB ABB ABC AAC

        a = get(0)
        b = get(1)
        c = get(2)

        ls = []
        # AAA
        # 0 < a + a + a < 2
        fc = a[0] + a[1] + a[2]
        ls.append(fc)

        # AAC
        # 0 < a + a < 1.5 and 0.75 < B < 1
        fc = a[3] + a[4] + c[3]
        ls.append(fc)

        # ABB
        fc = a[3] + b[3] + b[4]
        ls.append(fc)
        
        #ABC
        fc = a[3] + b[3] + c[3]
        ls.append(fc)

        #AAB
        fc = b[0] + a[3] + a[4]
        ls.append(fc)

        if a[0] != a[3]:
            fc = b[0] + a[0] + a[3]
            ls.append(fc)
            
            fc = b[3] + a[0] + a[3]
            ls.append(fc)
            
        fc = b[3] + a[0] + a[1]
        ls.append(fc)

        # check for overfolow and underflows
        for fc in ls:
            if fc > 1 and fc < 2:
                return 1
        return 0

A = [0.6, 0.7, 0.8, 1.2, 0.4]
print tripleSum(A)
