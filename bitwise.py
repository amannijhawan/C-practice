def bitwise(A, B, i, j):
    output = 0
    k = 0

    while(A):
        if (i<=k<=j):
            output = output&(B&1<<k)
            B=B>>1
            A=A>>1
        else:
            output = output&(A&1<<k)
            A=A>>1
    return output

result = bitwise(int('10000000000',2),int('10101',2),2,6)

def findmissing(A):
    