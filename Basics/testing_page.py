# this page is only for testing code:

thestr = "Ogres are often foolhardy oafs"
newstr = ""
for i, c in enumerate(thestr):
    if c == "o":
        continue
    if i > 20:
        break
    newstr += c
print(newstr)

for i in range(6, 15):
    print(i)
