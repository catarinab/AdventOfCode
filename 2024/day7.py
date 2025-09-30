import itertools

equations = []
combinations = {3: [('+'),('*'), ('|')]}

def part2():
    eqSum = 0
    for eq in equations:
        result = eq[0]
        if len(eq) not in combinations:
            combinations[len(eq)] = list(itertools.product('+*|', repeat=len(eq)-2))
        comb = combinations[len(eq)]
        for combination in comb:
            currResult = eq[1]
            for i in range(len(combination)):
                if(combination[i] == '+'):
                    currResult += eq[i+2]
                elif(combination[i] == '*'):
                    currResult *= eq[i+2]
                else:
                    currResult = int(str(currResult) + str(eq[i+2]))
            if(currResult == eq[0]):
                eqSum += currResult
                break
    return eqSum

def part1():
    eqSum = 0
    for eq in equations:
        result = eq[0]
        if len(eq) not in combinations:
            combinations[len(eq)] = list(itertools.product('+*', repeat=len(eq)-2))
        comb = combinations[len(eq)]
        for combination in comb:
            currResult = eq[1]
            for i in range(len(combination)):
                if(combination[i] == '+'):
                    currResult += eq[i+2]
                elif(combination[i] == '*'):
                    currResult *= eq[i+2]
            if(currResult == eq[0]):
                eqSum += currResult
                break
    return eqSum
            
        

def main():
    input_file = open("input/input.txt", "r")
    inputStrings = input_file.readlines()
    input_file.close()
    for string in inputStrings:
        line = list(string.strip().split(" "))
        line[0] = line[0][:-1]
        for i in range(len(line)):
            line[i] = int(line[i])
        equations.append(line)
        
    print(part2())
    
if __name__ == "__main__":
    main()