## Implement the quicksort algorithm and compute the number
##  of comparisons it makes while sorting a given list of 
##  integers.  The partition subroutine will choose the 
##  first integer in the array as the pivot point (Note:
##  this could be done in other ways)
lines = [line.strip() for line in open('QuickSort.txt')]
lines = map(int, lines) ## change to list of integers

## Partition subroutine options
## using extra memory and O(n) time, can initialize a new array and fill
## around pivot, larger integers to the right and smaller
## to the left
##
## Better solution: (constant time)
## Pivot stays in first position until finally swapped
##  into the correct location
tst = [10,9,18,2,1,6,0,3,4,5,99]

def partition(A):
    """ Partition array, pivoting on the first element, each element
    to the left is smaller than the pivot, each to the right
    is larger.
    """
    pivot = A[0]
    lessor, equal, greater = [], [], []
    for j in A:
        if j > pivot:
            greater.append(j)
        elif j < pivot:
            lessor.append(j)
        else:
            equal.append(j)
    return lessor, equal, greater

def quicksort(A):
    """ Quicksort algorithm using partition subroutine """
    if len(A) < 2:
        return A
    # partition A
    lessor, equal, greater = partition(A)
    # recurse on both sides of p
    return quicksort(lessor) + equal + quicksort(greater)

## quicksort but also counting the number of comparisons made to 
## the pivot
def quicksort1(A, count):
    """ Quicksort algorithm using partition subroutine """
    if len(A) < 2:
        return count
    # partition A
    count += len(A)-1
    lessor, equal, greater = partition(A)
    # recurse on both sides of p
    return quicksort1(lessor, count) + quicksort1(greater, count)

## quicksort with list comprehension
def qsort(A, count):
    if A == []: 
        return count
    count += len(A)-1
    ## compare to last elements instead of first:
    A[0],A[len(A)-1] = A[len(A)-1],A[0]
    pivot = A[0]
    l = qsort([x for x in A[1:] if x < pivot], count)
    u = qsort([x for x in A[1:] if x >= pivot], count)
    return l + u



def partition2(A):
    """ Partition array, pivoting on the first element, each element
    to the left is smaller than the pivot, each to the right
    is larger.
    """
    pivot = A[0]
    lessor, equal, greater = [], [], []
    i = 1
    j = 1
    while j < len(A):
        if A[j] > pivot:
            greater.append(A[j])
            j = j + 1
        elif A[j] < pivot:
            lessor.append(A[j])
            i = i + 1
            j = j + 1
    return lessor, equal, greater

## Another way, from class lecture
def partition3(A, left, right):
    count = len(A)-1
    pivot = A[left]
    i = left + 1
    for j in range(left+1, right):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i = i + 1
    pos = i - 1
    A[left], A[pos] = A[pos], A[left]
    return pos, A, count

def qsort3(A, left, right):
    if len(A) < 2:
        return 0, A
    pivot, A, count = partition3(A, left, right)
    countleft, Al = qsort3(A[:pivot], 0, len(A[:pivot]))
    countright, Ar = qsort3(A[pivot+1:], 0, len(A[pivot+1:]))
    return count+countleft+countright, Al+Ar

## Pivot from the last elements instead of the first
def partition4(A, left, right):
    count = right-left-1
    A[left],A[right-1] = A[right-1],A[left]
    pivot = A[left]
    i = left + 1
    for j in range(left+1, right):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i = i + 1
    pos = i - 1
    A[left], A[pos] = A[pos], A[left]
    return A[:pos], A[pos:], count

def qsort4(A, left, right):
    if len(A) < 2:
        return 0, A
    l, r, count = partition4(A, left, right)
    countleft, Al = qsort4(l, 0, len(l))
    countright, Ar = qsort4(r, 1, len(r))
    return count+countleft+countright, Al+Ar

## median of three as pivot
def partition5(A, left, right):
    count = right-left-1
    # choose pivot point
    p = choosePivot(A)
    A[left],A[p] = A[p],A[left]
    pivot = A[left]
    i = left + 1
    for j in range(left+1, right):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i = i + 1
    pos = i - 1
    A[left], A[pos] = A[pos], A[left]
    return A[:pos], A[pos:], count

def qsort5(A, left, right):
    if len(A) < 2:
        return 0, A
    l, r, count = partition5(A, left, right)
    countleft, Al = qsort5(l, 0, len(l))
    countright, Ar = qsort5(r, 1, len(r))
    return count+countleft+countright, Al+Ar

## set the recursion depth to test on already sorted list
import sys
sys.setrecursionlimit(20000)

## final versions, from text pseudocode
## this works, tested on already sorted as well
def part(A, p, r):
    x = A[p]
    i = p + 1
    for j in range(p+1, r):
        if A[j] <= x:
           A[i], A[j] = A[j], A[i]
           i = i + 1
    A[p], A[i-1] = A[i-1], A[p]
    return i-1

def qs(A, p, r):
    if A == []:
        return []
    if p < r:
        q = part(A, p, r)
        qs(A, p, q)
        qs(A, q + 1, r)

# now count number of comparisons, partitioning by the first
#  element of each array
def part1(A, p, r):
    x = A[p]
    i = p + 1
    for j in range(p+1, r):
        if A[j] <= x:
           A[i], A[j] = A[j], A[i]
           i = i + 1
    A[p], A[i-1] = A[i-1], A[p]
    return i-1

def qs1(A, p, r):
    if p < r:
        q = part1(A, p, r)
        return q-p-1 + r-q + qs1(A, p, q) + qs1(A, q + 1, r)
    else:
        return 0

# partition by the last element of each array
def part2(A, p, r):
    A[p], A[r-1] = A[r-1], A[p]
    x = A[p]
    i = p + 1
    for j in range(p+1, r):
        if A[j] <= x:
           A[i], A[j] = A[j], A[i]
           i = i + 1
    A[p], A[i-1] = A[i-1], A[p]
    return i-1

def qs2(A, p, r):
    if p < r:
        q = part2(A, p, r)
        return q-p-1 + r-q + qs2(A, p, q) + qs2(A, q + 1, r)
    else:
        return 0

# using median of first, middle, and last element as pivot
def choosePivot(A, p, r):
    if len(tst) % 2 == 0:
        middle = (len(A)//2)-1
    else:
        middle = len(A)//2
    if A[p] > A[middle] and A[p] < A[r-1]:
        pivot = p
    elif A[p] < A[middle] and A[p] > A[r-1]:
        pivot = p
    elif A[middle] > A[p] and A[middle] < A[r-1]:
        pivot = middle
    elif A[middle] < A[p] and A[middle] > A[r-1]:
        pivot = middle
    else:
        pivot = r-1
    return pivot

def part3(A, p, r):
    pivot = choosePivot(A, p, r)
    A[p], A[pivot] = A[pivot], A[p]
    x = A[p]
    i = p + 1
    for j in range(p+1, r):
        if A[j] <= x:
           A[i], A[j] = A[j], A[i]
           i = i + 1
    A[p], A[i-1] = A[i-1], A[p]
    return i-1

def qs3(A, p, r):
    if p < r:
        q = part3(A, p, r)
        return q-p-1 + r-q + qs3(A, p, q) + qs3(A, q + 1, r)
    else:
        return 0

lines = [line.strip() for line in open('QuickSort.txt')]
lines = map(int, lines) ## change to list of integers
