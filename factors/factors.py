import sys
def main():
    # Read the input file
    with open(sys.argv[1], 'r') as f:
        numbers = [int(line.strip()) for line in f]

    # Loop through all the numbers
    for n in numbers:
        # Try dividing n by every number from 2 to n
        for i in range(2, n+1):
            if n % i == 0:
                # Found a divisor, print the factorization and move on to the next number
                print(f"{n} = {i} * {n//i}")
                break
if __name__ == '__main__':
    main()
