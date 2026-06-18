# Comparative Study of Sorting Algorithms

## Team Members
- Nikolaos Katsikavalis 
- Georgios Papamikroulis 

## Description
This project is a theoretical and experimental study of three fundamental sorting algorithms: **Bubble Sort, Insertion Sort, and Merge Sort**, developed for the "Algorithms and Complexity" course. It analyzes their efficiency, complexity, and performance across various datasets based on descents and inversions.

## Key Findings
- **Complexity Verification:** Experimental data confirms the quadratic complexity $O(n^2)$ of Bubble and Insertion Sort, as well as the clear superiority of Merge Sort's O(n \log n) complexity on larger datasets.
- **Sensitivity to Initial Order:** Insertion Sort and the optimized Bubble Sort run exceptionally fast (close to O(n)) when the input array is already sorted.
- **Stability:** Merge Sort remains completely unaffected by the initial arrangement of the data, maintaining consistently low execution times regardless of whether the input is sorted, random, or reversed.

## Repository Contents
- `πρώτη_απαλλακτικη_εργασια_αλγόριθμοι.pdf`: The complete theoretical and experimental report.
- `B4erotima.py` & `Β3erotima2.py`: Functions for measuring and generating data with controlled descents/inversions.
- `erotimaG1G2.py`, `erotimaG3.py`, `G4erotima.py`: Algorithm implementations and benchmark experiments.
- `erotimaG5.py`: Python script utilizing Matplotlib to generate performance graphs.
