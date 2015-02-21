#!/usr/bin/env python
class SparseArray:
    def __init__(self):
        self.data = {}

    def __getitem__(self,k):
        if k in self.data: return self.data[k]
        else: return 0

    def __setitem__(self,k,v):
        if v==0:
            if k in self.data: del self.data[k]
        else: self.data[k] = v

    def __str__(self):
        kvs = []
        for k in self.data:
            v = self.data[k]
            kvs.append("{0}:{1}".format(k,v))
        return "{ %s }" % (",".join(kvs))

#Count the number of swaps to sort indices and get right sign, and xor indices to get return index
def destIdx(ai,bi):
    retidx, multiplier = ai^bi, 1
    stack, didSwap = [], True
    for i in [ai,bi]: #within an index, we order from right to left!!
        iidx = 0
        while i != 0:
            if i & 0b01:
                stack.append(iidx)
            i, iidx = i >> 1, iidx + 1
    while didSwap:
        didSwap = False
        for s in range(0,len(stack)-1):
            if stack[s] > stack[s+1]:
                stack[s], stack[s+1] = stack[s+1], stack[s]
                multiplier, didSwap = multiplier * -1, True
    return retidx, multiplier

#Multiplication is iterating over O( 2^(2d) ) possible contributions to place them in the right part of the result
def mul(d,a,b):
    answer = SparseArray()
    n = (1<<d) #only required to figure out how far to compute. Sparse arrays may tell us this too
    for ai in range(0,n):
        for bi in range(0,n):
            i, multiplier = destIdx(ai,bi)
            answer[i] += multiplier * a[ai] * b[bi]
    return answer

def add(d,a,b):
    answer = SparseArray()
    n = (1<<d)
    for ai in range(0,n):
        answer[ai] += a[ai] + b[ai]
    return answer

a=SparseArray()
a1=SparseArray()

a[0b001] = 1
a[0b010] = 2
a1[0b001] = 2
a1[0b100] = 3

#Checks out with example from: http://math.stackexchange.com/questions/916998/product-between-multivectors
print str(mul(3, a, a1))

