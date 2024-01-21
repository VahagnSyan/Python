data = [{'name': 'John','surname': 'Smith','age': 20,'phone':111},
        {'name': 'Mike', 'surname': 'Tyson', 'age': 21, 'phone':222},
        {'name': 'Jason', 'surname': 'Statham', 'age': 20, 'phone': 333}]

with open('result.csv', 'w', encoding='utf-8') as file:
    frow = tuple(data[0].keys())
    len_frow = len(frow)
    for i in range(len_frow):
        if i == len_frow - 1:
            file.write(str(frow[i]) + '\n')
        else:
            file.write(str(frow[i]) + ',')
    for j in data:
        row = tuple(j.values())
        len_row = len(row)
        for d in range(len_row):
            if d == len_row - 1:
                file.write(str(row[d]) + '\n')
            else:
                file.write(str(row[d]) + ',')
