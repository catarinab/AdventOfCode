
def part1(rules, pages):
    correctSum = 0
    ruleDict = {}
    for rule in rules:
        key = rule[0]
        item = rule[1]
        if(key in ruleDict):
            ruleDict[key].append(item)
        else:
            ruleDict[key] = [item]
    #print(ruleDict)
    #check each rule
    for page in pages:
        correct = True
        #print(page)
        for rule in ruleDict:
            try:
                firstIndex = page.index(rule)
                #print("rule:", rule, "FirstIndex: ", firstIndex)
                for item in ruleDict[rule]:
                    try:
                        secondIndex = page.index(item)
                        #print("secondNum", item, "secondIndex: ", secondIndex)
                        if(firstIndex > secondIndex):
                            correct = False
                            break
                    except:
                        continue
            except:
                continue
        if(correct):
            page = page.split(',')
            correctSum += int(page[int((len(page) - 1)/2)])

    return correctSum


def main():
    input_file = open("input/day5.txt", "r")
    inputStrings = input_file.readlines()
    input_file.close()
    rules, pages = [], []
    ispage = False
    for n in range(len(inputStrings)):
        inputStrings[n] = inputStrings[n].strip()
        if(inputStrings[n] == ""):
            ispage = True
            continue
        if(not ispage):
            rules.append(inputStrings[n].split('|'))
        else:
            pages.append(inputStrings[n])
    print(part1(rules, pages))

if __name__ == "__main__":
    main()