# naive search v binary search
import time

def naive_search(l, target):
    start_time = time.time()
    for i in range(len(l)):
        if l[i] == target:
            print((time.time() - start_time), ' seconds.')
            return i
    return -1

def binary_search(l, target, low=None, high=None):   # low and high are indicies, not values (starting low = 0, high = 4)
    start_time = time.time()
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    
    if high < low:
        return -1
    
    midpoint = (low + high) // 2
    
    if l[midpoint] == target:
        print((time.time() - start_time), ' seconds.')
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)

if __name__ == '__main__':
    l = range(1,1000000000000000)
    target = 765
    print("Index:", naive_search(l, 8654433))
    print("Index:", binary_search(l, 8654433))