# Each line in the input corresponds to a single bank of batteries
# In each bank, you need to turn on exactly two batteries.

def main():
    total_output = 0
    rows = 0
    with open('2025/day03/input.txt') as txtFile:
        for line in txtFile:
            bank_joltage = return_max_joltage(line)
            total_output += bank_joltage
            rows += 1

    print(f'Total output joltage (Password): {total_output}')   
    print(f'Rows: {rows}')

def return_max_joltage(line: str) -> int:
    line = line.strip()
    
    highestNumberOne = 0
    indexPlaceholder = 0
    for index, char in enumerate(line):
        number = int(char)
        if number > highestNumberOne:
            indexPlaceholder = index
            highestNumberOne = number

    lineBeforeIndex = line[:indexPlaceholder]
    lineAfterIndex = line[indexPlaceholder+1:]

    if lineBeforeIndex:
        numberBeforeIndex = max(int(c) for c in lineBeforeIndex)
        outcomeOne = int(str(numberBeforeIndex) + str(highestNumberOne))
    else:
        outcomeOne = 0 

    if lineAfterIndex:
        numberAfterIndex = max(int(c) for c in lineAfterIndex)
        outcomeTwo = int(str(highestNumberOne) + str(numberAfterIndex))
    else:
        outcomeTwo = 0  

    print(f'Line: {line}')
    print(f'Two outcomes. One: {outcomeOne} Two: {outcomeTwo}')
    print(f'Max outcome for this line: {max(outcomeOne, outcomeTwo)}\n')

    return max(outcomeOne, outcomeTwo)

main()
