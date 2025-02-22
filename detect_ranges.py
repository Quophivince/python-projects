#!/usr/bin/env python3

def detect_ranges(L):
    """
    Detects ranges in a list of integers and returns a list where intervals are represented as pairs.
    """
    # Sort the list
    L = sorted(L)
    result = []
    start = L[0]
    end = L[0]

    for i in range(1, len(L)):
        if L[i] == end + 1:
            # Extend the current interval
            end = L[i]
        else:
            # Add the interval or single number to the result
            if start == end:
                result.append(start)
            else:
                result.append((start, end + 1))
            # Start a new interval
            start = L[i]
            end = L[i]

    # Add the last interval or number
    if start == end:
        result.append(start)
    else:
        result.append((start, end + 1))

    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
