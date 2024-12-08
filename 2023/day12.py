from functools import lru_cache 

class Row:
    def __init__(self, springs, cont):
        self.springs = springs
        self.cont = cont
    
    def __str__(self):
        return self.springs + " -> " + str(self.cont) 
    

@lru_cache
def checkRow(spring, cont):
    if(len(spring) == 0): return len(cont) == 0
    
    if(spring[0] == '.'):
        return checkRow(spring[1:], cont)
    elif(spring[0] == '?'):
        return checkRow('#' + spring[1:], cont) + checkRow(spring[1:], cont)
    elif(spring[0] == '#'):
        if(len(cont) == 0): return 0

        ast = 0
        while(ast < len(spring) and spring[ast] != '.'): ast += 1    
        nextTry = int(cont.strip().split(',')[0])
        
        if nextTry <= ast:
            size = 2 if nextTry < 10 else 3
            cont = cont[size:]
            if(nextTry < len(spring) and spring[nextTry] != '#'):
                return checkRow(spring[nextTry+1:], cont)
            elif(nextTry == len(spring)):
                return checkRow('', cont)
            else:
                return 0
        else:
            return 0




f = open("/home/cat/uni/aoc23/inputs/day12.txt", "r")
lines = f.readlines()
f.close()


res = 0

for line in lines:
    cache = {}
    line = line.split(" ")
    cont = line[1].strip().split(',')
    initialCont = ','.join(cont)
    initialSpring = line[0]
    spring = initialSpring
    cont = initialCont
    for i in range(4):
        spring = spring + '?' + initialSpring
        cont = cont + ',' + initialCont
    row = Row(spring, cont)
    res += checkRow(row.springs, row.cont)
print(res)