import time
import sys
import random

sys.setrecursionlimit(10000)

# --- 1. ΑΛΓΟΡΙΘΜΟΙ ---
def bubble_sort(arr):
    comps = 0
    n = len(arr)
    start = time.perf_counter()
    for i in range(n - 1):
        swapped = False 
        for j in range(n - 1, i, -1):
            comps += 1
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True
        if not swapped:
            break # Τερματισμός αν η λίστα είναι ταξινομημένη
    return comps, time.perf_counter() - start

def insertion_sort(arr):
    comps = 0
    n = len(arr)
    start = time.perf_counter()
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        while i >= 0:
            comps += 1
            if arr[i] > key:
                arr[i+1] = arr[i]
                i -= 1
            else: break
        arr[i+1] = key
    return comps, time.perf_counter() - start

def merge(arr, p, q, r, stats):
    n1, n2 = q - p + 1, r - q
    L, R = arr[p:p+n1], arr[q+1:q+1+n2]
    L.append(float('inf')); R.append(float('inf'))
    i = j = 0
    for k in range(p, r + 1):
        stats['comps'] += 1
        if L[i] <= R[j]:
            arr[k] = L[i]; i += 1
        else:
            arr[k] = R[j]; j += 1

def merge_sort_recursive(arr, p, r, stats):
    if p < r:
        q = (p + r) // 2
        merge_sort_recursive(arr, p, q, stats)
        merge_sort_recursive(arr, q + 1, r, stats)
        merge(arr, p, q, r, stats)

def merge_sort(arr):
    stats = {'comps': 0}
    start = time.perf_counter()
    merge_sort_recursive(arr, 0, len(arr) - 1, stats)
    return stats['comps'], time.perf_counter() - start

# --- 2. ΓΕΝΝΗΤΡΙΕΣ ΔΕΔΟΜΕΝΩΝ ---
def create_descents(n, k):
    data = list(range(1, n + 1))
    data[:k+1] = reversed(data[:k+1])
    return data

def generate_all_datasets(n):
    return {
        "Sorted": list(range(1, n + 1)),
        "Reverse": list(range(n, 0, -1)),
        "Random": random.sample(range(1, n * 10), n),
        "Few_Descents": create_descents(n, max(1, int(n * 0.1))),
        "Many_Descents": create_descents(n, int(n * 0.8))
    }

# --- 3. ΠΕΙΡΑΜΑ ---
def run_full_experiment():
    sizes = [100, 500, 1000, 2000, 5000]
    iterations = 10
    algos = {"Bubble Sort": bubble_sort, "Insertion Sort": insertion_sort, "Merge Sort": merge_sort}
    final_stats = {}

    print("Εκτέλεση πειραμάτων (10 επαναλήψεις ανά περίπτωση)...")
    
    for n in sizes:
        print(f"Μετρήσεις για n = {n}...")
        datasets = generate_all_datasets(n)
        for name, func in algos.items():
            if name not in final_stats: final_stats[name] = {}
            final_stats[name][n] = {}
            for d_type, d_list in datasets.items():
                t_sum = 0
                for _ in range(iterations):
                    _, t = func(d_list.copy())
                    t_sum += t
                final_stats[name][n][d_type] = t_sum / iterations

    print("\n" + "="*80)
    print(f"{'Αλγόριθμος':<15} | {'n':<6} | {'Τύπος':<15} | {'Χρόνος (s)':<15}")
    print("-" * 80)
    for a in final_stats:
        for n in sizes:
            for d in final_stats[a][n]:
                print(f"{a:<15} | {n:<6} | {d:<15} | {final_stats[a][n][d]:.6f}")
    return final_stats

if __name__ == "__main__":
    results = run_full_experiment()