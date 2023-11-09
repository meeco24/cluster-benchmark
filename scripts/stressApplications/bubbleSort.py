import numpy as np
import time

def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		if not swapped:
			return

def main():
    while(1):
        dim = np.random.randint(8,11)
        array = np.random.randint(low=0, high=100, size=(dim))
        
        print(dim)
        bubbleSort(array)
        print(array)
        
        time.sleep(5)

if __name__ == '__main__':
    main()