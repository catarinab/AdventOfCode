from itertools import product

class Row:
    def __init__(self, springs, cont):
        self.springs = springs
        self.cont = cont
    
    def __str__(self):
        return self.springs + " -> " + str(self.cont) 
    

def changeString(s, i, c):
    return s[:i] + c + s[i+1:]

def checkRow(spring, cont, matches = 0, order = []):

    #print("processing: " + spring + " with " + str(cont))

    if(len(spring) == 0):
        if(len(cont) == 0):
            #print("MATCHHH")
            #print(order)
            return matches + 1
        else:
            return matches


   
    
    if(spring[0] == '.'):
        #print("string: " + spring+ "generated " + spring[1:], " currOrder: " + str(order))
        matches = checkRow(spring[1:], cont, matches)
    elif(spring[0] == '?'):
        #print("string: " + spring+ "generated "+ '#' + spring[1:] + "and "+ '.' + spring[1:], " currOrder: " + str(order))
        matches = checkRow('#' + spring[1:], cont, matches, order)
        matches = checkRow('.' + spring[1:], cont, matches, order)
    elif(spring[0] == '#'):
        if(len(cont) == 0): return matches


        ast = 0
        while(ast < len(spring) and (spring[ast] == '#' or spring[ast] == '?')):
            ast += 1    
        
        nextTry = cont[0]
        #print("trying: " + str(nextTry))
        tempCont = [k for k in cont]
        if nextTry <= ast:
            tempCont.remove(nextTry)
            #print("string: " + spring+ " generated:")
            if(nextTry < len(spring) and spring[nextTry] != '#'):
                spring = '.'+spring[nextTry+1:]
            elif(nextTry == len(spring)):
                spring = ''
            else:
                return matches
                #print("nao da")
                #print(nextTry, len(spring), spring)
            #print(spring)
            order.append(nextTry)
            matches = checkRow(spring, tempCont, matches)
            order.pop()

    return matches




f = open("/home/cat/uni/aoc23/inputs/day12.txt", "r")
lines = f.readlines()
f.close()

#lines = [lines[1]]
res = 0
for line in lines:
    line = line.split(" ")
    cont = line[1].strip().split(',')
    cont = [int(i) for i in cont]
    row = Row(line[0], cont)
    print(row)
    currRes = checkRow(row.springs, row.cont)
    print(currRes)
    res += currRes

print(res)