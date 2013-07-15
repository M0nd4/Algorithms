## max subarray problem using divide and conquer

## create some sample data, 10000 integers between 0 and 10000,
##  each entry can be a day, calculate the pair with the max diff,
##  10000
import random
tst = random.sample(xrange(10000),10000)

# brute force
# try every two-way comparison: O(n**2)
def brute_force_maxArray(A):
    """ try every comparison: n choose 2, O(n**2) runtime
    """
    best = 0
    bestdays = (0,0)
    for i,j in enumerate(A):
        for k,l in enumerate(A):
            if A[i]-A[k] > best:
                best = A[i]-A[k]
                bestdays = (i,k)
    return [bestdays, best]

## divide and conquer approach
# first transform the array to be a daily change from left to right
tst2 = [tst[i+1]-tst[i] for i in xrange(len(tst)-1)]
def find_max_crossing_subarray(A, low, mid, high):
    """Finds the maximum subarray that crosses the mid-point
    runs in linear time O(n)"""
    leftsum = -10000
    maxleft = -10000
    sum = 0
    for i in range(low,mid):
        sum += A[mid-i]
        if sum > leftsum:
            leftsum = sum
            maxleft = mid-i
    rightsum = -10000
    maxright = -10000
    sum = 0
    for j in range(mid, high):
        sum += A[j]
        if sum > rightsum:
            rightsum = sum
            maxright = j
    return (maxleft, maxright, leftsum+rightsum)

## Procedure to find the maximum subarray, divide and conquer,
#  using find_max_crossing_subarray to calculate worst case
def find_max_subarray(A,low,high):
    if low == high:
        return (low, high, A[low])
    else:
        mid = (low+high)//2
        (leftlow, lefthigh, leftsum) = find_max_subarray(A,low,mid)
        (rightlow, righthigh, rightsum) = find_max_subarray(A,mid+1,high)
        (crosslow,crosshigh,crosssum) = find_max_crossing_subarray(A,low,mid,high)
    if leftsum >= rightsum and leftsum >= crosssum:
        return(leftlow, lefthigh, leftsum)
    if rightsum >= leftsum and rightsum >= crosssum:
        return(rightlow, righthigh, rightsum)
    else:
        return (crosslow, crosshigh, crosssum)
