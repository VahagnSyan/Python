"""
    Write a function that will count the number of 
    occurrences of letters in a
    string and return it as a dictionary․

"""

def count_elements(list):
    list1 = dict()
    for element in list:
        list1[element] = list1.get(element, 0) + 1 

    return list1

string = input('Enter the string: ')
print(count_elements(string))  
