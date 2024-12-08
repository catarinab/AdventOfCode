f = open("inputs/day4.txt", "r")
lines = f.readlines()
f.close()

finalSum = 0

class Ticket:
    def __init__(self, id, value, copies):
        self.id = id
        self.value = value
        self.copies = copies


tickets = [Ticket(i, 0, 1) for i in range(len(lines))]

for i in range(len(lines)):
    lines[i] = lines[i].strip()
    currLine = lines[i].split("|")
    winningNums = currLine[1].strip().split()
    winningNums = [int(x) for x in winningNums]

    # Check if the ticket is valid
    myNums = currLine[0].split(":")[1].split()
    myNums = [int(x) for x in myNums]
    
    matches = 0
    for num in myNums:
        if num in winningNums:
            matches += 1

    for idx in range(i + 1, tickets[i].id + matches + 1):
        tickets[idx].copies += tickets[i].copies
    
    finalSum += tickets[i].copies

print(finalSum)