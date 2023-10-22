class Solution:
    def IsPerfect(self,arr,n):
        reversed_arr = arr[::-1]

    # Check if the original and reversed arrays are the same
        if arr == reversed_arr:
            return True
        else:
            return False



for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    if(ob.IsPerfect(arr,n)):
        print("PERFECT")
    else:
        print("NOT PERFECT")
    