import numpy as np
import matplotlib.pyplot as plt
from typing import List


def thinning(lambda_max: float, T: float) -> List[float]:
    """
    Generuje niejednorodny proces Poissona na przedziale [0, T] za pomocą metody przerzedzeń.

    Parameters:
        lambda_max (float): Maksymalna wartość funkcji intensywności.
        T (float): Czas końcowy.

    Returns:
        List[float]: Lista zawierająca czasy przyjścia zdarzeń.
    """
    S = []
    t = 0
    while (t := t - np.log(np.random.uniform()) / lambda_max) <= T:
        S.append(t)
    return S


T = 20
arr = thinning(lambda_max=0.8, T=T)

# Wykres procesu Poissona
plt.figure(figsize=(10, 5))
plt.step(arr, range(len(arr)))
plt.xlabel("Czas")
plt.ylabel("Liczba przybyć")
plt.title("Niejednorodny proces Poissona (metoda przerzedzeń)")
plt.grid(True)
plt.show()
