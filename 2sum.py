## The 2-Sum Problem, week 6 problem 1
## Task: Given 1 million integer input array, compute the 
##  number of target values, t in the interval [-10000,10000] 
##  (inclusive) that are distinct numbers x,y that satisfy the 
##  condition x+y=t.
##
## Input: unsorted array of integers. Target sum t.
##
## Simple solution: go over all n choose 2 pairs and check sum,
##  quadratic runtime.
## Better solution: 
##  1. sort integers up front (mergesort, quicksort) O(n log n)
##  2. for each entry in array, A, look for complementary entry t-x
##   in A via a binary search, O(n log n)
##
## Best solution: use hash table for lookup
##  1. insert elements into hash table H, O(n)
##  2. for each x in A, lookup t-x in H, O(n)

lines = [line.strip() for line in open('algo1_programming_prob_2sum.txt')]
lines = map(int, lines) ## change to list of integers

## use dictionary to implement hash lookup
A = {a:a for a in lines}

count = 0
for t in range(-10000,10001):
    if t%50 == 0:
        print(t)
    for x in A:
        if t-x in A:
            count += 1
            print(count)
            break
## count = 427, hours to run though

count = 0
for t in range(-100,100):
    if t%50 == 0:
        print(t)
    for x in A:
        if t-x in A:
            count += 1
            print(count)
            break
## count = 5
