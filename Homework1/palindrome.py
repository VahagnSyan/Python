a = "dshsdkdshsd"
length = len(a)
condition_met = True

for i in range(length // 2):
    if a[i] != a[length - i - 1]:
        condition_met = False
        break

if condition_met:
    print("true")
else:
    print("false")
