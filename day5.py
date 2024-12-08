from collections import defaultdict, deque

def topological_sort(ruleDict, ruleIndices):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    newRuleDict = {k: [v for v in values if v in ruleIndices] 
                for k, values in ruleDict.items() if k in ruleIndices}
    
    
    for key, values in newRuleDict.items():
        for value in values:
            graph[key].append(value)
            in_degree[value] += 1
            in_degree[key] = in_degree.get(key, 0)
    
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return order

def part1(rules, pages):
    correctSum = 0
    ruleDict = {}
    incorrectPages = []
    for rule in rules:
        key = rule[0]
        item = rule[1]
        if(key in ruleDict):
            ruleDict[key].append(item)
        else:
            ruleDict[key] = [item]
    for page in pages:
        correct = True
        for rule in ruleDict:
            try:
                firstIndex = page.index(rule)
                for item in ruleDict[rule]:
                    try:
                        secondIndex = page.index(item)
                        if(firstIndex > secondIndex):
                            correct = False
                            break
                    except:
                        continue
            except:
                continue
        page = page.split(',')
        if(correct):
            correctSum += int(page[int((len(page) - 1)/2)])
        else:
            incorrectPages.append(page)
    return incorrectPages, ruleDict, correctSum

def part2(ruleDict, incorrectPages):
    wrongSum = 0
    for page in incorrectPages:
        ruleIndices = []
        for rule in ruleDict:
            if(rule in page):
                ruleIndices.append(rule)
        orderedRules = topological_sort(ruleDict, ruleIndices)
        
        for i in range(len(orderedRules)):
            index = page.index(orderedRules[i])
            page[index], page[i] = page[i], page[index]

        wrongSum += int(page[int((len(page) - 1)/2)])

    return wrongSum
    

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
    incorrectPages, ruleDict, correctSum = part1(rules, pages)
    print(correctSum)
    print(part2(ruleDict, incorrectPages))

if __name__ == "__main__":
    main()