## Row Reduction algorithm for matrix
##
## Plan:
## 1. select the row with largest absolute value coefficient in 
##   leftmost row, move row to top
## 2. Use row replacement operations to replace all coefficients
##   with 0s below the pivot in leading column
## 3. Repeat process on remaining rows in matrix
## 
## To create reduced echelon matrix
## 4. Beginning with rightmost pivot and working upward and to the
##   left, create zeros above each pivot. 
## 5. Make each pivot = 1 by scaling operations 
