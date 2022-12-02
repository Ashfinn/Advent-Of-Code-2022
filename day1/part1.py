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

print(max(new))

input_txt.close()
