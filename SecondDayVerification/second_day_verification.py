import sys

def solve():
    # Read a line from standard input
    # Assume input consists of two space-separated integers
    line = sys.stdin.readline().strip()

    # If the line is empty, do nothing (or handle as an error, depending on problem specifics)
    if not line:
        return

    try:
        # Parse the two integers
        val1, val2 = map(int, line.split())

        # Perform the "verification": check if the second value is strictly greater than the first
        # This simulates verifying an improvement from "Day 1" to "Day 2"
        if val2 > val1:
            print(True)
        else:
            print(False)
    except ValueError:
        # Handle cases where input is not in the expected format (e.g., not two integers)
        # For competitive programming, valid input format is usually guaranteed,
        # so this block might not be strictly necessary but is good practice.
        pass

# Call the solve function to execute the solution
solve()