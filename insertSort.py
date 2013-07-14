# Insertion sort algorithm
#  O(n**2)
#  but quick for small applications
test = [5,4,3,2,1]
for j in range(1,len(test)):
    key = test[j]
    # add the key into the sorted subarray
    i = j - 1
    while i > -1 and test[i] > key:
        test[i + 1] = test[i]
        i = i - 1
    test[i + 1] = key
