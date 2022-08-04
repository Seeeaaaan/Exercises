import re
handle = open('REact.txt')
avalue = 0
for line in handle:
    line = line.rstrip()
    datas = re.findall('[0-9]+', line)
    for number in datas:
        number = int(number)
        avalue = avalue + number
print(avalue)