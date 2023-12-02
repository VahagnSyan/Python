'''
    write a function that returns the number of 
    non-overlapping occurrences of substring sub in string S
    i.e. write a function that does the same as a builtin str.count() function does
    function signature: count_sub_in_str(string_obj, substring)
'''

def count_sub_in_str(string_obj, substring):
    count = 0  
    str_len = len(string_obj) 
    sub_len = len(substring)  
    
    if sub_len <= str_len:  
        i = 0  
        while i <= str_len - sub_len:  
            # Check if the substring starting at index i matches the given substring
            if string_obj[i:i + sub_len] == substring:
                count += 1  
                i += sub_len  
            else:
                i += 1  
    
    return count  

string = input("Enter the text: ")
sub_str = input("What I have to find: ")
print("Count:", count_sub_in_str(string, sub_str))

