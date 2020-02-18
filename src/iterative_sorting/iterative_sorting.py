import random
# TO-DO: Complete the selection_sort() function below 
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [0, 1, 2, 3, 4, 5]
arr4 = random.sample(range(200), 50)

def selection_sort( arr ):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):
    # 1. Start with current index = 0
        smallest_index = i
        # 2. For all indices EXCEPT the last index:
        #     a. Loop through elements on right-hand-side 
        #     of current index and find the smallest element
        for j in range(i, len(arr) - 1):
            # CHECK WHICH NUMBER IS SMALLER AND MAKE SURE SOON-TO-BE SMALLEST_INDEX IS SMALLER THAN THE CURRENT SMALLEST_INDEX
            if arr[j + 1] < arr[i] and arr[j + 1] < arr[smallest_index]:
                smallest_index = j + 1
        #     b. Swap the element at current index with the
        #     smallest element found in above loop
        if smallest_index != i:
            num = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = num
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps = 0
    swapping = True
    while swapping:
        swaps = 0
        if len(arr) > 0:
            # 1. Loop through your array
                # - Compare each element to its neighbor
            for i in range(0, len(arr) - 1):
                j = i + 1
                # - If elements in wrong position (relative to each other, swap them)
                if arr[i] > arr[j]:
                    swapping = True
                    swaps += 1
                    num = arr[i]
                    arr[i] = arr[j]
                    arr[j] = num
                # 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1
                elif arr[i] < arr[j] and swaps == 0:
                    swapping = False
        else:
            swapping = False

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # CREATE AN ARRAY OF THE LENGTH OF THE ARRAY
    sorted_arr = [l for l in range(0, len(arr))]
    # CREATE AN ARRAY WITH ALL ZEROS EQUAL TO THE LENGTH OF THE MAXIMUM NUMBER
    for i in range(0, len(arr) - 1):
        maximum = i
        for j in range(0, len(arr) - 1):
            if arr[maximum] < arr[j + 1]:
                maximum = arr[j + 1]
    init_arr = [0 for l in range(0, maximum)]
    for k in range(0, len(arr)):
        init_arr[arr[k]] += 1;
    total = 0;
    for l in range(0, maximum):
        oldCount = init_arr[l];
        init_arr[l] = total;
        total += oldCount;
    for m in range(0, len(arr)):
        sorted_arr[init_arr[arr[m]]] = arr[m];
        init_arr[arr[m]] += 1
        arr[m] = sorted_arr[m]
                



    return arr

print(count_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))