# USEFUL VIDEOS ON MERGE SORTING:
    # https://www.youtube.com/watch?v=xF3TU-QlhJQ
    # https://www.youtube.com/watch?v=4VqmGXwpLqc

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( left, right, arr ):
    '''
        A helper function that handles merging sorted pieces back together
    '''
    # 3. Start merging your single lists of one element together into larger, sorted sets

    i = 0
    j = 0
    k = 0

    while (i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
    
        k += 1
    
    while(i < len(left)):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while(j < len(right)):
        arr[k] = right[j]
        j += 1
        k += 1

    return arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    '''
        A recursive function that handles dividing the array (or subarray) in half
    '''
    # 1. While your data set contains more than one item, split it in half
    # 2. Once you have gotten down to a single element, you have also *sorted* that element (a single element cannot be "out of order")
    # 4. Repeat step 3 until the entire data set has been reassembled

    if len(arr) < 2:
        return arr
    else:
        left = [n for n in arr[:len(arr) // 2]]
        right = [n for n in arr[len(arr) // 2:]]
        
        merge_sort(left)
        merge_sort(right)

    return merge(left, right, arr)

# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
