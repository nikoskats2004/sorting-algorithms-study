import time
import sys
import random

sys.setrecursionlimit(10000)

def bubble_sort(arr):
    # Δραστηριότητα Γ.2: Μετρητές συγκρίσεων και χρόνου
    comparisons = 0
    n = len(arr)
    start_time = time.perf_counter()
    
    for i in range(n - 1):
        swapped = False # Προσθήκη για αρμονία με τη θεωρία (Α.1)
        for j in range(n - 1, i, -1):
            comparisons += 1
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
        if not swapped:
            break # Σταματάει αν ο πίνακας είναι ήδη ταξινομημένος
                
    end_time = time.perf_counter()
    duration = end_time - start_time
    return comparisons, duration

def insertion_sort(arr):
    # Δραστηριότητα Γ.2: Μετρητές συγκρίσεων και χρόνου
    comparisons = 0
    n = len(arr)
    start_time = time.perf_counter()
    
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0:
            comparisons += 1
            if arr[i] > key:
                arr[i + 1] = arr[i]
                i -= 1
            else:
                break
        arr[i + 1] = key
        
    end_time = time.perf_counter()
    duration = end_time - start_time
    return comparisons, duration

def merge_sort_recursive(arr, p, r, stats):
    if p < r:
        q = (p + r) // 2
        merge_sort_recursive(arr, p, q, stats)
        merge_sort_recursive(arr, q + 1, r, stats)
        merge(arr, p, q, r, stats)

def merge(arr, p, q, r, stats):
    n1 = q - p + 1
    n2 = r - q
    L = arr[p:p + n1]
    R = arr[q + 1:q + 1 + n2]
    
    L.append(float('inf'))
    R.append(float('inf'))
    
    i = 0
    j = 0
    for k in range(p, r + 1):
        stats['comps'] += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

def merge_sort(arr):
    # Δραστηριότητα Γ.2: Μετρητές συγκρίσεων και χρόνου
    stats = {'comps': 0}
    start_time = time.perf_counter()
    
    merge_sort_recursive(arr, 0, len(arr) - 1, stats)
    
    end_time = time.perf_counter()
    duration = end_time - start_time
    return stats['comps'], duration

if __name__ == "__main__":
    n = 1000
    test_data = [random.randint(1, 10000) for _ in range(n)]
    
    print(f"--- Πειραματική Μελέτη (n={n}) ---")
    
    c_b, t_b = bubble_sort(test_data.copy())
    print(f"Bubble Sort    -> Συγκρίσεις: {c_b}, Χρόνος: {t_b:.6f}s")
    
    c_i, t_i = insertion_sort(test_data.copy())
    print(f"Insertion Sort -> Συγκρίσεις: {c_i}, Χρόνος: {t_i:.6f}s")
    
    c_m, t_m = merge_sort(test_data.copy())
    print(f"Merge Sort     -> Συγκρίσεις: {c_m}, Χρόνος: {t_m:.6f}s")