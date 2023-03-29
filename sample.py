def Pattern(dimen):
     
    # arr[][] will store the pattern matrix
    arr = [[0 for row in range(dimen)]
              for col in range(dimen)]
    value = 1
 
    # Store the values for upper
    # triangle of the pattern
    for k in range(dimen):
        row = k
        col = 0
        while (row >= 0):
            arr[row][col] = value
            value += 1
            row  -= 1
            col  += 1
     
    # Store the values for lower triangle of the pattern
    for k in range(1, dimen, 1):
        col = k
        row = dimen - 1
        f = k
        while (row >= f):
            arr[row][col] = value
            value += 1
            row -= 1
            col += 1
     
    # Print the pattern
    for row in range(0, dimen, 1):
        for col in range(0, dimen, 1):
            print(arr[row][col], end = " ")
         
        print("\n", end = "")
 
# Driver code
if __name__ == '__main__':
   dimen = 4
 
   Pattern(dimen)