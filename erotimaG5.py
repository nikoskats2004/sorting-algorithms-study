import time
import sys
import random
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)

# --- 1. ΑΛΓΟΡΙΘΜΟΙ (Επιστρέφουν Συγκρίσεις & Χρόνο) ---
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
            break # Σταματάει αν ο πίνακας είναι ήδη ταξινομημένος 
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

def generate_datasets(n):
    return {
        "Sorted": list(range(1, n + 1)),
        "Few_Descents": create_descents(n, max(1, int(n * 0.1))),
        "Random": random.sample(range(1, n * 10), n),
        "Many_Descents": create_descents(n, int(n * 0.8)),
        "Reverse": list(range(n, 0, -1))
    }

# --- 3. ΔΙΕΞΑΓΩΓΗ ΠΕΙΡΑΜΑΤΟΣ ---
def run_experiments_for_graphs():
    sizes = [100, 500, 1000, 2000] 
    iterations = 5 
    algos = {"Bubble Sort": bubble_sort, "Insertion Sort": insertion_sort, "Merge Sort": merge_sort}
    
    results = {a: {n: {} for n in sizes} for a in algos}

    print("Συλλογή δεδομένων για τα γραφήματα.")
    for n in sizes:
        print(f" -> Εκτέλεση για n={n}...")
        datasets = generate_datasets(n)
        for a_name, func in algos.items():
            for d_name, d_data in datasets.items():
                tot_c = tot_t = 0
                for _ in range(iterations):
                    c, t = func(d_data.copy())
                    tot_c += c
                    tot_t += t
                results[a_name][n][d_name] = {'comps': tot_c / iterations, 'time': tot_t / iterations}
    
    return sizes, results

# --- 4. ΣΧΕΔΙΑΣΗ ΓΡΑΦΗΜΑΤΩΝ (Δραστηριότητα Γ.5)  ---
def plot_results(sizes, results):
    # Γράφημα 1: Χρόνος ως προς n (για Τυχαία ακολουθία) [cite: 63]
    plt.figure(figsize=(10, 6))
    for algo in results:
        times = [results[algo][n]["Random"]['time'] for n in sizes]
        plt.plot(sizes, times, marker='o', label=algo)
    plt.title("Γράφημα 1: Χρόνος Εκτέλεσης ως προς το μέγεθος n (Τυχαία Ακολουθία)")
    plt.xlabel("Μέγεθος n")
    plt.ylabel("Χρόνος (δευτερόλεπτα)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Γράφημα 2: Συγκρίσεις ως προς n (για Τυχαία ακολουθία) [cite: 64]
    plt.figure(figsize=(10, 6))
    for algo in results:
        comps = [results[algo][n]["Random"]['comps'] for n in sizes]
        plt.plot(sizes, comps, marker='s', label=algo)
    plt.title("Γράφημα 2: Αριθμός Συγκρίσεων ως προς το μέγεθος n (Τυχαία Ακολουθία)")
    plt.xlabel("Μέγεθος n")
    plt.ylabel("Αριθμός Συγκρίσεων (Λογαριθμική Κλίμακα)")
    plt.yscale('log') 
    plt.legend()
    plt.grid(True)
    plt.show()

    # Γράφημα 3: Επίδραση των Descents στην απόδοση [cite: 65]
    plt.figure(figsize=(10, 6))
    target_n = 2000
    categories = ["Sorted", "Few_Descents", "Random", "Many_Descents", "Reverse"]
    display_names = ["Ταξινομημένη (0)", "Λίγα Descents", "Τυχαία", "Πολλά Descents", "Αντίστροφη (Max)"]
    
    for algo in results:
        times = [results[algo][target_n][cat]['time'] for cat in categories]
        plt.plot(display_names, times, marker='^', label=algo)
    
    plt.title(f"Γράφημα 3: Επίδραση Αριθμού Descents στον Χρόνο (n={target_n})")
    plt.xlabel("Βαθμός Αταξίας (Πλήθος Descents/Αντιστροφών)")
    plt.ylabel("Χρόνος (δευτερόλεπτα)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    s, r = run_experiments_for_graphs()
    plot_results(s, r)