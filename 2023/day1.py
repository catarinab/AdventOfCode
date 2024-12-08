f = open("inputs/day1.txt", "r")
lines = f.readlines()
f.close()

nums = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, 
        "seven": 7, "eight": 8, "nine": 9}

matches = ["zero", "one", "two", "three", "four", "five", "six", 
        "seven", "eight", "nine", "ten"]

sum = 0

for i in range(len(lines)):
    first = 0
    last = 0
    found = False
    currString = ""
    for char in lines[i]:
        if char.isnumeric():
            currString = ""
            if(found == False):
                first = int(char)
                last = int(char)
                found = True
            else:
                last = int(char)
        else:
            currString += char
            res = [ele for ele in matches if(ele in currString)]
            if(len(res) != 0):
                if(found == False):
                    first = nums[res[0]]
                    last = nums[res[0]]
                    found = True
                else:
                    last = nums[res[0]]
                currString = currString[-1]
    sum += first*10 + last
print(sum)
