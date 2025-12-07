def main():
    txtFile = open('2025/day02/input.txt')

    invalidIdCount = 0

    IdRanges = txtFile.read().split(',')

    for idRange in IdRanges:
        idStartAndEnd = idRange.split('-')
        idStart = int(idStartAndEnd[0])
        idEnd = int(idStartAndEnd[1])
        rangeOfIds = int(idEnd - idStart)
        # print(f'Total range: {idRange}')
        # print(f'Start: {idStart}')
        # print(f'End: {idEnd}')
        # print(f'Range: {rangeOfIds}')
        for step in range(rangeOfIds):
            id = str(idStart + step)
            idLength = int(len(id))
            half = idLength // 2
            if(id[0:half] == id[half:]):
                invalidIdCount += 1
   
    print(f"Count of invalid ID's: {invalidIdCount}")

main()