strat = open("day2/input.txt", "r")
list = strat.read()
list2 = list.split('\n')

points = 0
for i in list2:

    if i == 'A X':    
        points += 3
    elif i == 'B Y':    
        points += 5
    elif i == 'C Z':    
        points += 7

    elif i == 'A Z':      
        points += 8
    elif i == 'B X':      
        points += 1
    elif i == 'C Y':      
        points += 6
  
    elif i == 'A Y':         
        points += 4
    elif i == 'B Z':         
        points += 9
    elif i == 'C X':         
        points += 2

print(points)

strat.close()