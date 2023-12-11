f = open("inputs/day6test.txt", "r")
lines = f.readlines()
f.close()

times = lines[0].split(":")[1].split()
distances = lines[1].split(":")[1].split()

time = ""
distance = ""


for item in times:
    time += item
currTime = int(time)

for item in distances:
    distance += item
raceLen = int(distance)

result = 1
wins = 0
prevDistance = 0
for i in range(raceLen):
    raceTime = currTime - i
    if(raceTime <= 0):
        break
    totalDistance = i * raceTime
    if(totalDistance > raceLen):
        wins += 1
    
    prevDistance = totalDistance
result *= wins
print(result)