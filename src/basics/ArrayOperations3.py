from numpy import *
arr1 = array([1, 2, 3, 4, 5])
arr2 = array([2, 3, 4, 5, 6])
arr3 = array([5, 3, 6, 7, 10])
# arr1 = arr1 * arr2
print(sqrt(arr1))
print(arr1 * arr1)
print(concatenate([arr3, arr2, arr1]))
arr4 = arr1.view()        # creates an array's copy of same memory address ( shallow copy )
print(arr4)
arr5 = arr2.copy()    # creates an array's copy of different memory address ( deep copy )
print(arr5)
