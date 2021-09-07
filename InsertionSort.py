def insertionSort(arr):
   
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr = []
for i in range(0,6):
    n=input()
    arr.append(n)
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print(arr)
    break