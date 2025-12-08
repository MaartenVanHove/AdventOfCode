def main():
    txtFile = open('2025/day02/input.txt')
    invalidIdCount = 0

    idRanges = txtFile.read().strip().split(',')

    for idRange in idRanges:
        idStartAndEnd = idRange.split('-')
        idStart = int(idStartAndEnd[0])
        idEnd = int(idStartAndEnd[1])

        for num in range(idStart, idEnd + 1):
            id = str(num)

            if (len(id) % 2 != 0): continue

            idLength = int(len(id))

            half = idLength // 2
            if(id[0:half] == id[half:]):
                invalidIdCount += int(id)
   
    print(f"Count of invalid ID's: {invalidIdCount}")

main()