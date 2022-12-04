comp = open("day3/input.txt", "r")
c = comp.read()
li = c.split("\n")

for i in li:
    if i == "":
        li.remove(i)
    

print(li)

comp.close()