from turtle import clear


fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    SL = line.split()
    for LS in SL:
        if LS not in lst:
            lst.append(LS)
lst.sort()
print(lst)