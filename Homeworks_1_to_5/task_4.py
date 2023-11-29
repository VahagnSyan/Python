'''
Print the following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
# DefinE the number of rows for the pattern
rows = 5
# Define the loop counter
i = 1

# Loop for each row
while i <= rows:
    j = 1

    # Loop for printing numbers in each row
    while j <= i:
        # Print the value of the outer loop counter (i) with a space
        print(i, end=' ')
        j += 1

    # Move to the next line after printing the numbers for the current row
    print()
    i += 1
