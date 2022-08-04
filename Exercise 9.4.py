name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
tae = dict()
bcount = None
bsender = None
for send in handle:
    if send.startswith("From "):
        word = send.split()
        tae[word[1]] = tae.get(word[1], 0) + 1
    else:
        continue
for sender,count in tae.items():
    if bcount is None or count > bcount:
        bcount = count
        bsender = sender
print(bsender, bcount)

#OR YOU CAN ALSO USE THE CODE :

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
tae = dict()
bcount = None
bsender = None
for send in handle:
    if send.startswith("From"):
        tae[send] = tae.get(send, 0) + 1
    else:
        continue
for sender,count in tae.items():
    if bcount is None or count > bcount:
        sender = sender.split()
        bcount = count
        bsender = sender[1]
print(bsender, bcount)