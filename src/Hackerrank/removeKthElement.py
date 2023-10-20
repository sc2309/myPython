def remove(arr, n, k):
    n=n-1
    k=k-1
    arr[k],arr[n-k] = arr[n-k],arr[k]
    for i in range(n+1):
        print(arr[i],end=' ')

n, k = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))

remove(arr, n, k)
