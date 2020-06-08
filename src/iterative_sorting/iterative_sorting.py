# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

        # instructors solution:
        #arr[curr_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swapped = True

    while swapped:
        swapped = False

        for i in range(len(arr) - 1):
            j = i + 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def count_sort(arr, maximum=None):
    maximum = 0
    for el in arr:
        if el < 0:
            return "Error, negative numbers not allowed in Count Sort"

        if (el > maximum):
            maximum = el 

    counts = [0] * (maximum + 1)

    for el in arr:
        counts[el] += 1
    
    newIndex = 0
    for el in enumerate(counts):
        i, count = el

        while count > 0:
            arr[newIndex] = i
            newIndex += 1
            count -= 1

    return arr


sample = [3, 4, 1, 8, 3, 8, 34, -32, -2, 21, 8, 1, 0, 34, 32]
test = count_sort(sample)

print(test)
