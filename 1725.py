def f (idx,area):
    stack = []
    stack.append(arr[idx])

    while stack :
        width = 1
        compare = stack.pop()
        while compare < arr[idx+width] :
            idx += 1
            
     
     
N = int(input())
maxV = 0
arr = []
sol = []
for i in range(N) :
    arr.append(int(input()))

for i in range(N):
    f(i,0)





