def count_descents(A):
    # Μέτρηση περιπτώσεων όπου A[i] > A[i+1]
    count = 0
    for i in range(len(A) - 1):
        if A[i] > A[i+1]:
            count += 1
    return count

def count_inversions(A):
    # Μέτρηση ζευγών (i, j) με i < j και A[i] > A[j]
    count = 0
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                count += 1
    return count

# Δοκιμή με τη λίστα της άσκησης
if __name__ == "__main__":
    test_list = [2, 1, 3, 5, 4]
    print(f"Δεδομένα εισόδου: {test_list}")
    print(f"Πλήθος Descents: {count_descents(test_list)}")
    print(f"Πλήθος Αντιστροφών: {count_inversions(test_list)}")
