# Each line in the input corresponds to a single bank of batteries
# In each bank, you need to turn on exactly twelve batteries.

def main():
    total_jotage = 0
    with open('2025/day03/input.txt') as txtFile:

        for line in txtFile:
            bank_joltage = return_output(line)
            total_jotage += bank_joltage
        print(f'Total joytage: {total_jotage}')

        # return_output("1233318223444255434472644637233422336336412424363623253447431632444277334744421343233631466233334454")


def return_output(line: str) -> int:
    line = line.strip()   
    lengthLine = len(line)         
    batteries = 12
    output = ''
    startIndex = 0

    for i in range(batteries):
        largest = '0'            
        
        offset = lengthLine - (batteries - i)
        print(f'Full length: {lengthLine} Offset: {offset} battery: {i}')
        print(f'Start Index: {startIndex}')
        newLine = line[startIndex:offset + 1]

        bestIndex = None
        for index, num in enumerate(newLine):
            if num > largest:
                largest = num
                bestIndex = index 


        startIndex = startIndex + bestIndex + 1
        output += largest

    print(f'Output: {output}')
    return int(output)


main()