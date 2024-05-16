import numpy as np
import matplotlib.pyplot as plt
from typing import List
from scipy.integrate import quad


def thinning(lambda_t, lambda_max: float, T: float) -> List[float]:
    """
    Generuje niejednorodny proces Poissona na przedziale [0, T] za pomocą metody przerzedzeń.

    Parameters:
        lambda_t (callable): Funkcja intensywności w zależności od czasu.
        lambda_max (float): Maksymalna wartość funkcji intensywności.
        T (float): Czas końcowy.

    Returns:
        List[float]: Lista zawierająca czasy przyjścia zdarzeń.
    """
    S = []
    t = 0
    while (t := t - np.log(np.random.uniform()) / lambda_max) <= T:
        if np.random.uniform() < lambda_t(t) / lambda_max:
            S.append(t)
    return S


def lambda_t(t: float) -> float:
    """
    Funkcja intensywności.

    Parameters:
        t (float): Czas.

    Returns:
        float: Wartość funkcji intensywności w punkcie czasowym t.
    """
    return 5 + 0.5 * np.sin(2 * np.pi * t / 24)


def mean_arrivals(lambda_t, T: float) -> float:
    """
    Oblicza średnią liczbę przyjść dla niejednorodnego procesu Poissona.

    Parameters:
        lambda_t (callable): Funkcja intensywności w zależności od czasu.
        T (float): Czas końcowy.

    Returns:
        float: Średnia liczba przyjść.
    """
    result, _ = quad(lambda_t, 0, T)
    return result / T


def mean_time_at_T(
    lambda_t, lambda_max: float, T: float, num_realizations: int
) -> float:
    """
    Oblicza średnią wartość czasu w chwili T dla 1000 realizacji niejednorodnego procesu Poissona.

    Parameters:
        lambda_t (callable): Funkcja intensywności w zależności od czasu.
        lambda_max (float): Maksymalna wartość funkcji intensywności.
        T (float): Czas końcowy.
        num_realizations (int): Liczba realizacji.

    Returns:
        float: Średnia wartość czasu w chwili T.
    """
    times_at_T = []
    for _ in range(num_realizations):
        arrivals = thinning(lambda_t, lambda_max, T)
        if arrivals:
            times_at_T.append(arrivals[-1])
    return np.mean(times_at_T)


T = 20
lambda_max = np.max([lambda_t(t) for t in np.linspace(0, T, 1000)])
mean_integrated_value = mean_arrivals(lambda_t, T)
arr = thinning(lambda_t, lambda_max, T)
num_realizations = 1000
mean_time_value = mean_time_at_T(lambda_t, lambda_max, T, num_realizations)
mean_arrivals_value = mean_arrivals(lambda_t, T)

print("Średnia wartość czasu w chwili T (całka):", mean_integrated_value)
print("Średnia wartość czasu w chwili T (1000 realizacji):", mean_time_value)

# Wykres procesu Poissona
plt.figure(figsize=(10, 5))
plt.step(arr, range(len(arr)))
plt.xlabel("Czas")
plt.ylabel("Liczba przybyć")
plt.title("Niejednorodny proces Poissona (metoda przerzedzeń)")
plt.grid(True)
plt.show()
