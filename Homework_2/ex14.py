#Returns the set which keys are the string elements and the values are teir counts in the string  
def get_symbol_frequency(string):
    resault = {}
    for i in string:
        if i in resault:
            resault[i] += 1
        else:
            resault[i] = 1
    return resault


string = input("Enter the text: ")
resault = get_symbol_frequency(string)

print(resault)

