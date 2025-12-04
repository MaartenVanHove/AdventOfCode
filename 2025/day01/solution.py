def main():
    txtFile = open('2025/day01/input.txt')

    startNumber = 50
    dialNumber = startNumber
    zeroCounter = 0

    print(f'startNumber: {dialNumber}')

    for line in txtFile:
        dial = line.strip()
        distance = int(dial[1:])
        if(dial[0] == 'L'):
            dialNumber -= distance
        elif(dial[0] == 'R'):
            dialNumber += distance

        dialNumber %= 100
        print(dialNumber)

        if(dialNumber == 0):
            zeroCounter += 1
            
    print(f'Zero counter: {zeroCounter}')

main()
