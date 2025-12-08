# Each line in the input corresponds to a single bank of batteries
# In each bank, you need to turn on excatly two batteries.

def main():
    with open('2025/day03/input.txt') as txtFile:
        count = 0
        for line in txtFile:
            count += return_max_joltage(line)
            print(count)

        print(f'Password {count}')   

def return_max_joltage(line: int) -> int:
    highestNumberOne = 0
    indexPlaceholder = 0
    for index, char in enumerate(line.strip()):
        number = int(char)
        if number > highestNumberOne:
            indexPlaceholder = index
            highestNumberOne = number

    numberBeforeIndex = 0
    numberAfterIndex = 0
    lineBeforeIndex = line[:indexPlaceholder]
    lineAfterIndex = line[indexPlaceholder+1:]

    for index, char in enumerate(lineBeforeIndex.strip()):
        number = int(char)
        if(number > numberBeforeIndex):
            numberBeforeIndex = number
    outcomeOne = int(str(numberBeforeIndex) + str(highestNumberOne))

    for index, char in enumerate(lineAfterIndex.strip()):
        number = int(char)
        if number > numberAfterIndex:
            numberAfterIndex = number
    outcomeTwo = int(str(highestNumberOne) + str(numberAfterIndex))

    print(f'Line: {line.strip()}')
    print(f'Two outcomes. One: {outcomeOne} Two: {outcomeTwo}')
    print(f'Outcome: {max(outcomeOne, outcomeTwo)}')

    return max(outcomeOne, outcomeTwo)

main()