def main():
    with open('2025/day02/input.txt') as txtFile:

        ranges = txtFile.read().strip().split(',')
        total = 0

        for r in ranges:
            start, end = map(int, r.split('-'))

            for num in range(start, end + 1):
                if is_repeated_pattern(num):
                    total += num
        
        print(f"Password: {total}")

def is_repeated_pattern(number: int) -> bool:
    s = str(number)
    ss = (s + s)[1: -1]

    return s in ss

main()