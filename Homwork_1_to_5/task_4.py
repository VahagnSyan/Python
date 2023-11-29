'''
Print the following pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
# Define the number of rows for the pattern
rows = 5
# Define the loop counter
i = 1

#Loop through the elements
while i <= rows:
    # Print a string with numbers 1 to i, repeated i times
    print((str(i) + ' ') * i)
    # Add the node counter
    i += 1
