#!/usr/bin/env python3

def merge(L1, L2):
    """
    Merges two sorted lists L1 and L2 into a single sorted list.
    """
    merged_list = []
    i, j = 0, 0

    # Use two pointers to iterate through both lists
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged_list.append(L1[i])
            i += 1
        else:
            merged_list.append(L2[j])
            j += 1

    # Add remaining elements from L1 or L2
    while i < len(L1):
        merged_list.append(L1[i])
        i += 1
    while j < len(L2):
        merged_list.append(L2[j])
        j += 1

    return merged_list

def main():
    # Example inputs
    L1 = sorted([1, 3, 5, 7, 9])
    L2 = sorted([2, 4, 6, 8, 10])

    # Test the merge function
    print("L1:", L1)
    print("L2:", L2)
    merged = merge(L1, L2)
    print("Merged List:", merged)

    # Another test case
    L3 = sorted([1, 2, 3])
    L4 = sorted([4, 5, 6])
    print("L3:", L3)
    print("L4:", L4)
    merged2 = merge(L3, L4)
    print("Merged List:", merged2)

if __name__ == "__main__":
    main()
