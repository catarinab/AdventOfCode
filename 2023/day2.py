f = open("inputs/day2.txt", "r")
lines = f.readlines()
f.close()

sum = 0

for i in range(len(lines)):
    parts = lines[i].split(":")
    id = parts[0].split(" ")[1]
    parts = parts[1].split(";")
    
    vals = {"red": 0, "green": 0, "blue": 0}

    for reveals in parts:
        rev = reveals.split(",")
        for ele in rev:
            ele = ele.strip().split(" ")
            val = ele[0]
            color = ele[1]
            if(int(val) > vals[color]):
                vals[color] = int(val)

    sum += vals["red"] * vals["green"] * vals["blue"]
        
print(sum)
