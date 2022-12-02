strat = open("day2/input.txt", "r")
list = strat.read()
list2 = list.split('\n')

points = 0
for i in list2:
    #draw
    if i == 'A X':    
        points += 4
    elif i == 'B Y':    
        points += 5
    elif i == 'C Z':    
        points += 6
    #draw
    #enemy wins
    elif i == 'A Z':      
        points += 3
    elif i == 'B X':      
        points += 1
    elif i == 'C Y':      
        points += 2
    #enemy wins
    #we win
    elif i == 'A Y':         
        points += 8
    elif i == 'B Z':         
        points += 9
    elif i == 'C X':         
        points += 7
    #we win

print(points)

strat.close()