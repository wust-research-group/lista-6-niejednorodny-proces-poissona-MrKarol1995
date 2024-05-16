import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List

def generate_marked_poisson(lambda_max: float, T: float, pk: List[float]) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generuje znacznikowy proces Poissona na przedziale [0, T].

    Parameters:
        lambda_max (float): Maksymalna intensywność procesu Poissona.
        T (float): Czas trwania procesu.
        pk (list): Lista prawdopodobieństw dla każdego znacznika.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Krotka zawierająca tablicę czasów przyjść zdarzeń i tablicę znaczników odpowiadających przybyciom zdarzeń.
    """
    arrivals = []
    marks = []
    t = 0
    while t < T:
        u1 = np.random.uniform()
        inter_arrival_time = -np.log(u1) / lambda_max
        t += inter_arrival_time
        if t < T:
            k = np.random.choice(len(pk), p=pk)
            arrivals.append(t)
            marks.append(k+1)  # Indeksowanie znaczników od 1
    return np.array(arrivals), np.array(marks)

# Parametry
lambda_max = 0.8
T = 20
pk = [0.4, 0.3, 0.3]  # Prawdopodobieństwa dla każdego znacznika

# Generowanie znacznikowego procesu Poissona
arrivals, marks = generate_marked_poisson(lambda_max, T, pk)

# Tworzenie tablicy dla każdego znacznika
unique_marks = np.unique(marks)
mark_arrivals = [arrivals[marks == mark] for mark in unique_marks]

# Rysowanie wykresu
plt.figure(figsize=(10, 5))
for i, mark in enumerate(unique_marks):
    plt.step(mark_arrivals[i], np.arange(len(mark_arrivals[i])) + 1, label=f'Znacznik {mark}')
plt.xlabel('Czas')
plt.ylabel('Liczba zdarzeń')
plt.title('Znacznikowy proces Poissona')
plt.legend()
plt.grid(True)
plt.show()
