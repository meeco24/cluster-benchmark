import numpy as np
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main(): 
    while(1):
        dim = np.random.randint(198,200)
        array = np.random.randint(low=0, high=600, size=(dim))
        
        print(dim)
        insertion_sort(array)

        time.sleep(5)


if __name__ == '__main__':
    main()    