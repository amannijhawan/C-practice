# Search in a matrix whose rows and columns are sorted already

matrix =[
       [1,5,10,15,],
       [2,6,11,16,],
       [3,7,12,17,],
       [4,8,13,18,],
]

def find_item(item, matrix,size):
    searchcol = None
    for (j,elt) in enumerate(matrix[0]):
        if item == elt:
            return (0,j)
        else:
            if j>0:
                if matrix[0][j-1]<item<elt:
                    searchcol = j-1
                    break
    if searchcol is None:
        searchcol = j  
    if searchcol is not None:
        for i in range(size):
            if matrix[i][searchcol] == item:
                return (i,searchcol)
    return None

print find_item(12,matrix,4)
print find_item(18,matrix,4)
print find_item(13,matrix,4)

               
