import random

def create_descents(n, k):
  
    data = list(range(1, n + 1))
    data[:k+1] = reversed(data[:k+1])
    return data

def generate_all_datasets(n):
    datasets = {}
    
    # 1. Ήδη ταξινομημένη ακολουθία
    datasets["Sorted"] = list(range(1, n + 1))
    
    # 2. Αντίστροφα ταξινομημένη ακολουθία
    datasets["Reverse"] = list(range(n, 0, -1))
    
    # 3. Τυχαία ακολουθία
    datasets["Random"] = random.sample(range(1, n * 10), n)
    
    # 4. Ακολουθία με μικρό αριθμό descents 
    k_small = max(1, int(n * 0.1))
    datasets["Few_Descents"] = create_descents(n, k_small)
    
    # 5. Ακολουθία με μεγάλο αριθμό descents
    k_large = int(n * 0.8)
    datasets["Many_Descents"] = create_descents(n, k_large)
    
    return datasets

if __name__ == "__main__":
    n_test = 10
    data = generate_all_datasets(n_test)
    for name, s in data.items():
        print(f"{name:15}: {s}")