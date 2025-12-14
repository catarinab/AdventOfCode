import re

def part2(number):
    numbers = []
    for i in range(len(str(number))):
        numbers.append((int(number[i]), i))
    #choose starting number
    start = (numbers[0][0], 0)
    idx = 0
    while(idx < len(numbers)- 11):
        if(numbers[idx][0] > start[0]):
            start = numbers[idx]
        idx += 1
    voltage = str(start[0])
    popVal = len(numbers) - 12 - start[1]
    numbers = numbers[start[1]+1:]
    numbers = sorted(numbers, key=lambda x: x[0])
    numbers = numbers[popVal:]
    numbers = sorted(numbers, key=lambda x: x[1])
    for n in numbers:
        voltage += str(n[0])
    return int(voltage)

def part1(number):
    bestVoltage = 0
    if(re.search(r'9.*9', number)):
        return 99
    for startingrange in range(len(str(number))-2, -1, -1):
        n1 = number[startingrange]
        n2 = number[startingrange+1]
        for n in range(startingrange+2, len(str(number))):
            if(int(number[n]) > int(n2)):
                n2 = number[n]
        voltage = n1+n2
        if(int(voltage) > int(bestVoltage)):
            bestVoltage = voltage
    return int(bestVoltage)
    
input_file = open("input/day3.txt", "r")
lines = input_file.readlines()
input_file.close()
p1 = 0
p2 = 0
for line in lines:
    number = line.strip()
    p1 += part1(number)
    p2 += part2(number)
print("Total Voltage: ", p1)
print("Total Sum: ", p2)