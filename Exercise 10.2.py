name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = list()
counts = dict()
for word in handle :
    if word.startswith('From '):
        half = word.split()
        tae = half[5]
        time = tae[:2]
        counts[time] = counts.get(time, 0) + 1
    else :
        continue
for t, c in counts.items() :
    count.append((t, c))
trash = sorted(count)
for (hours, times) in trash:
    print(hours, times)