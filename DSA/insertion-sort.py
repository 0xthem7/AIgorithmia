A = [5, 2, 4, 6, 1, 3]
n = len(A)

for i in range(1, n):
    key = A[i] # 2
    j = i - 1 # 5
    while j > 0 and A[j] > key:
        A[i] = A[j]
        j = j-1
    A[j+1] = j 
print(A)


