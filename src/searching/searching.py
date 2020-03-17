import math

# STRETCH: implement Linear Search				
def linear_search(arr, target):
  if target in arr:
    return arr.index(target)
  else:
    return -1   # not found

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1
  while True:
      mid = high // 2
      if target < arr[mid]:
          high = mid
      elif target > arr[mid]:
          low = mid
      elif target == arr[mid]:
          return mid
      else:
          return -1 # not found

# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
