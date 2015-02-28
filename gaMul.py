#!/usr/bin/env python

dims = 5

class MultiVector:
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
            kvs.append(("{0:0%db}:{1}" % dims).format(k,v))
        return "{ %s }" % (", ".join(kvs))

    def __iter__(self):
        for k in self.data:
            yield k

    #This only supports ORTHOGONAL basis, of a large number of dimensions
    def destIdx(self, ai,bi):
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

    def mul(self,b):
        a = self
        d =  dims
        answer = MultiVector()
        for ai in a:
            for bi in b:
                i, multiplier = self.destIdx(ai,bi)
                answer[i] += multiplier * a[ai] * b[bi]
        return answer

    def add(self,b):
        a = self
        d = dims
        answer = MultiVector()
        for ai in a:
            answer[ai] += a[ai] + b[ai]
        return answer

a=MultiVector()
a1=MultiVector()

a[0b001] = 1
a[0b010] = 2
a1[0b001] = 2
a1[0b100] = 3

#Checks out with example from: http://math.stackexchange.com/questions/916998/product-between-multivectors
print str(a)
print str(a1)
print str(a.mul(a1))

