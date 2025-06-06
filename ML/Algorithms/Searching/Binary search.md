---
tags:
  - search
  - algorithms
---
- **What is it?**: A searching algorithm.
- **Input**: Sorted list of elements.
- **Output**
	- If element in list : Position of the said elements.
	- If element not in list : `null`.
- **Logarithmic time**: Execution time increases slowly, but steadily with input size. 
	- Time -> Goes up linearly
	- n -> Goes up exponentially
- **Big-O notation**: O (log n)

![[Pasted image 20250502105937.png]]
```py
import numpy as np

def binary_search(array, num):
    low = 0
    high = len(array) - 1
    while (low<=high):
        mid = (low + high)
        guess = array[mid]
        if (guess<num):
            print("Too low!")
            low = mid + 1
        elif (guess>num):
            print("Too high!")
            high = mid - 1
        else:
            print(f"The number is at position: {mid}")
            return "Done"
    return None
```
