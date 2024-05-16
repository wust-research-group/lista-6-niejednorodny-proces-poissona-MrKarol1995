import numpy as np
import matplotlib.pyplot as plt
from typing import List, Callable

def thinning(lambda_t: Callable[[float], float], lambda_max: float, T: float) -> List[float]:
    """
    Generuje niejednorodny proces Poissona na przedziale [0, T] za pomocą metody przerzedzeń.

    Parameters:
        lambda_t (Callable[[float], float]): Funkcja intensywności w zależności od czasu.
        lambda_max (float): Maksymalna wartość funkcji intensywności.
        T (float): Czas końcowy.

    Returns:
        List[float]: Lista zawierająca czasy przyjścia zdarzeń.
    """
    S = []
    t = 0
    while (t := t - np.log(np.random.uniform()) / lambda_max) <= T:
        u = np.random.uniform()
        if u < lambda_t(t) / lambda_max:
            S.append(t)
    return S



def lambda_t1(t: float) -> float:
    """
    Funkcja intensywności dla pierwszego procesu.

    Parametry:
        t (float): Czas.

    Zwraca:
        float: Intensywność w czasie t.
    """
    return t


def lambda_t2(t: float) -> float:
    """
    Funkcja intensywności dla drugiego procesu.

    Parametry:
        t (float): Czas.

    Zwraca:
        float: Intensywność w czasie t.
    """
    return t**2 / 10


def lambda_t_combined(t: float) -> float:
    """
    Połączona funkcja intensywności dla obu procesów.

    Parametry:
        t (float): Czas.

    Zwraca:
        float: Połączona intensywność w czasie t.
    """
    return t + t**2 / 10


T = 20

# Generowanie procesów Poissona dla lambda_t1 i lambda_t2
arrivals1 = thinning(lambda_max=0.8, T=T, lambda_t=lambda_t1)
arrivals2 = thinning(lambda_max=0.8, T=T, lambda_t=lambda_t2)

# Połączenie wszystkich zdarzeń
combined_arrivals = np.concatenate((arrivals1, arrivals2))
combined_arrivals.sort()

# Generowanie procesu Poissona dla lambda_t_combined
arrivals_combined = thinning(lambda_max=1.1, T=T, lambda_t=lambda_t_combined)

# Porównanie wszystkich wykresów na jednym
plt.figure(figsize=(10, 5))
plt.step(arrivals1, range(len(arrivals1)), label="Proces 1", where="post", color="blue")
plt.step(arrivals2, range(len(arrivals2)), label="Proces 2", where="post", color="green")
plt.step(combined_arrivals, range(len(combined_arrivals)), label="Połączone Procesy", where="post", color="red")
plt.step(arrivals_combined, range(len(arrivals_combined)), label="Proces Poissona (lambda_t_combined)", where="post", color="purple")
plt.xlabel("Czas")
plt.ylabel("Liczba Przybyć")
plt.title("Porównanie Procesów Poissona")
plt.legend()
plt.grid(True)
plt.show()

time_points = np.linspace(0, T, 1000)
intensity1 = lambda_t1(time_points)
intensity2 = lambda_t2(time_points)
intensity_combined = lambda_t_combined(time_points)

# Wykresy intensywności
plt.figure(figsize=(10, 5))
plt.plot(time_points, intensity1, label="Proces 1", color="blue")
plt.plot(time_points, intensity2, label="Proces 2", color="green")
plt.plot(time_points, intensity_combined, label="Połączone Procesy", color="red")
plt.xlabel("Czas")
plt.ylabel("Intensywność")
plt.title("Porównanie Intensywności Procesów Poissona")
plt.legend()
plt.grid(True)
plt.show()
