## Fast Divide and Conquer Algorithm to count the number
##  of inversions in an array of integers

## get file with 100000 integers
tst = open('IntegerArray.txt')
f = list(tst)

## reading lines of a file to a list
with open('IntegerArray.txt') as f:
    content = f.readlines()

## stripping newline characters and reading file by line to a list
lines = [line.strip() for line in open('IntegerArray.txt')]
lines = map(int, lines) ## change to list of integers

# test cases
L1 = list(range(0,10)) ## no inversions
L2 = [10,9,1,2,5] ## 7 inversions


# Simple form of the algorithm (no divide and conquer)
def simple_count_inversions (intList):
    """O(n^2) inversion counting"""
    return sum(k > intList[j]
               for (i, k) in enumerate(intList)
               for j in xrange(i+1, len(intList)))

# fast version: divide into two, recursively sort, merge back together
def merge_and_count(a, b):
    assert a == sorted(a) and b == sorted(b) # checks they are sorted
    print(a)
    print(b)
    c = []
    count = 0
    i, j = 0, 0
    while i < len(a) and j < len(b):
        c.append(min(b[j], a[i]))
        if b[j] < a[i]:
            count += len(a) - i # number of elements remaining in `a`
            j+=1
        else:
            i+=1
    # now we reached the end of one the lists
    c += a[i:] + b[j:] # append the remainder of the list to C
    return count, c

def sort_and_count(L):
    if len(L) == 1: return 0, L
    n = len(L) // 2 
    a, b = L[:n], L[n:]
    ra, a = sort_and_count(a)
    rb, b = sort_and_count(b)
    r, L = merge_and_count(a, b)
    return ra+rb+r, L
