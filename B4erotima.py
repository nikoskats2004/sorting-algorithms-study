def create_descents(n, k):
    # Δημιουργία λίστας n στοιχείων με k descents
    if k < 0 or k >= n:
        return "Error: k must be between 0 and n-1"
    
    # Αρχική αύξουσα λίστα
    data = list(range(1, n + 1))
    
    # Αντιστροφή τμήματος για δημιουργία descents
    data[:k+1] = reversed(data[:k+1])
    
    return data

def create_inversions(n, k):
    # Δημιουργία λίστας n στοιχείων με k αντιστροφές
    limit = n * (n - 1) // 2
    if k < 0 or k > limit:
        return f"Error: k must be between 0 and {limit}"
    
    source = list(range(1, n + 1))
    result = []
    
    for i in range(n):
        # Υπολογισμός διαθέσιμων θέσεων στα δεξιά
        slots = n - 1 - i
        
        if k >= slots:
            # Επιλογή μεγαλύτερου στοιχείου
            val = source.pop()
            result.append(val)
            k -= slots
        else:
            # Επιλογή στοιχείου για ακριβή συμπλήρωση του k
            val = source.pop(k)
            result.append(val)
            k = 0
            
    return result

# Παραδείγματα εκτέλεσης
if __name__ == "__main__":
    n, k_des, k_inv = 8, 3, 12
    
    print(f"Λίστα με {k_des} descents: {create_descents(n, k_des)}")
    print(f"Λίστα με {k_inv} inversions: {create_inversions(n, k_inv)}")