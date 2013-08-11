## Median Maintanence Algorithm
## The problem:
 # Letting xi denote the ith number of the file, the kth median mk is defined as the median of the numbers x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk; if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

lines = [line.strip() for line in open('Median.txt')]
lines = map(int, lines) ## change to list of integers

## Input: A stream of numbers, represented by priority queues
##
## Outline: At each time step, i, compute the median of {x1,..xi}
## Constraint: Use O(log i) at each time step
##
## Gampeplan: Use two heaps, one that with extrac-min one with
##  extract-max, maintain the invariant that the i/2 smallest
##  (largest) are in the Heap_low (Heap_high)
##
## Psuedocode:
##  1. Initialize two heaps, for each incoming number, 
##     compare to extract-max(Heap_low)
##   and extract-min(Heap_high)
##  2. Insert in proper heap
##  3. If two numbers inserted into the same heap in a row,
##      extract one number from that heap and add to other heap.
##  4. Compute median, if i is odd median is extracted from larger
##     heap, if i is even extract-min from Heap_high

## test case, answer should be 55 (sum of medians)
tst = [10,1,9,2,8,3,7,4,6,5]
tst2 = lines[:8193] # median(sum of median) = 4964(37819470)
from heapq import *
heap_high = [] # has extract-min capability
heap_low = [] # stored as negative values, so extract-min becomes max
medians = [] # list of medians, new median with each new number
previous = 0 # 0 if last entry added to low, 1 if added to high
stream = tst2
median = 0
for i in range(1,len(stream)+1):
    if i == 1:
        heappush(heap_low,-stream[i-1])
    else:
        if stream[i-1] > -heap_low[0]:
            heappush(heap_high,stream[i-1])
        else:
            heappush(heap_low, -stream[i-1])
    if len(heap_high) > len(heap_low):
        transfer = heappop(heap_high)
        heappush(heap_low,-transfer)
    if len(heap_low) > len(heap_high)+1:
        transfer = heappop(heap_low)
        heappush(heap_high,-transfer)
    medians = medians+[-heap_low[0]]
    median = -heap_low[0]

## answer: (sum(medians))%10000 = 1213
