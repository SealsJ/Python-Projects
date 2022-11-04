import random
import time

#naive search through a list which isn't as productive
def naive_search(l, target):
    #Example list [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
        
    return -1

#binary search divides and conquers through a list, leverage the fact that list is SORTED
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    # example l = [1, 3, 5, 10, 12] #if target is 10 should return 3
    midpoint = (low + high) // 2 #// gives rounded value should be 2 to approximate midpoint
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else: 
        #target > l(midpoint)
        return binary_search(l, target, midpoint + 1, high)


if __name__=='__main__':
    # l = [1, 3, 5, 10, 12]
    # target = 10
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    length = 10000
    #build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end-start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end-start)/length, "seconds")

