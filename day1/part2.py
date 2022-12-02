input_txt = open("day1\input.txt", "r")
inpt = input_txt.read()
i= inpt.split('\n')

new = []
num = 0
for j in range(len(i)):
    if i[j] == '':
        new.append(num)
        num = 0
        continue
    num+= int(i[j])
new.append(num)
new.sort(reverse=True)

maxes = [new[0], new[1], new[2]]
print(sum(maxes))

input_txt.close()
