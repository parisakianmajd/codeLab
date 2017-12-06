# Given the number of rows, generate the first numRows of Pascal's triangle.
from math import factorial
from itertools import combinations


class Pascal:
    def __init__(self, size):
        self.size = size


    def generate(self):
        a = self.size
        if a == 0:
            return []
        if a == 1:
            return [[1]]
        triangle = [[1]]
        for row in xrange(1, a):
            newRow = [1]
            for i in xrange(1,row):
                newRow.append(triangle[-1][i -1] + triangle[-1][i])
            newRow.append(1)
            triangle.append(newRow)
        return triangle
    
    def generate2(self):
        triangle = []
        for r in xrange(self.size):
            row = []
            for i in xrange(r):
                row.append(factorial(r) / ((factorial(i)) * factorial(r - i)))
            triangle.append(row)
        return triangle

    def generate3(self):
        triangle = []
        for r in xrange(self.size):
            row = []
            for i in xrange(r):
                row.append(len(list(combinations(range(r), i))))
            triangle.append(row)
        return triangle


    def getRow(self, A):
            row = [1]
            if A == 0:
                return row
            # C(n,k+1) = C(n,k) * (n-k) / (k+1)
            for k in xrange(A):
                row.append(row[k] * (A-k) / (k+1))
            return row
    def generate4(self):
        triangle = []
        for r in xrange(self.size):
            row = []
            for i in xrange(r):
                row=self.getRow(i)
            triangle.append(row)
        return triangle     
    
    def draw(self):
        triangle = self.generate()
        n = self.size
        width = len(' '.join(map(str, triangle[-1])))
        for i in xrange(n):
            row = ' '.join(map(str, triangle[i]))
            rowSize = len(row)
            print ' ' * ((width-rowSize)/2) + row + ' ' * ((width-rowSize)/2)

        

                            
pascal = Pascal(5)
pascal.draw()
