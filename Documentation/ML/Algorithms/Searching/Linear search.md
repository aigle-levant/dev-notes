---
tags: [algorithms]
---
- **Linear time**: Maximum no. of guess = size of the list.
- **Big-O notation**: O(n)

```py
import numpy as np

def linear_search(array, n):
    array_length = len(array)-1
    for i in range(0, array_length):
        if array[i]==n:
            return (f"{n} is at position {i}")
        else:
            print("Still searching!")
```
